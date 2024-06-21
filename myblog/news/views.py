import django_filters
from django import forms
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import BaseFilterBackend
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Likes, Comments
from .form import CommentsForm
from django.views import View
from django.views.generic.base import TemplateView
from .serializers import PostSerializer


class PostView(TemplateView):
    template_name = 'news/news.html'  # Шаблон, который будет использоваться для отображения контента

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['post_list'] = posts
        return context

# Create your views here.
class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'news/news_detail.html', {'post': post})

class AddComments(View):
    '''Добавление комментариев'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['email', 'name', 'text_comments']

    def clean_text_comments(self):
        text_comments = self.cleaned_data.get('text_comments')
        min_length = 10  # Минимальная длина текста комментария

        if len(text_comments) < min_length:
            raise forms.ValidationError(f'Text comments must be at least {min_length} characters long.')

        return text_comments

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

class PostApiViewPagination(PageNumberPagination):
    page_size = 5;
    page_query_param = 'page size';
    max_page_size = 10000;

class UserPostsFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)

class CustomFilterBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)
        # Получите значения из URL и примените к вашему queryset
        param_value = request.query_params.get('param_name')
        if param_value:
            kwargs['queryset'] = queryset.filter(field_name=param_value)
        return kwargs

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostApiViewPagination
    filter_backends = [CustomFilterBackend]

class LikeApiAdd(APIView):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            existing_like = Likes.objects.get(ip=ip_client, post_id=pk)
            return Response({'message': 'Like already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Likes.DoesNotExist:
            new_like = Likes(ip=ip_client, post_id=pk)
            new_like.save()
            return Response({'message': 'Like added successfully'}, status=status.HTTP_201_CREATED)

class LikeApiDel(APIView):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like_to_delete = Likes.objects.get(ip=ip_client, post_id=pk)
            like_to_delete.delete()
            return Response({'message': 'Like deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Likes.DoesNotExist:
            return Response({'message': 'Like does not exist'}, status=status.HTTP_404_NOT_FOUND)
