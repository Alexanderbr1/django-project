import django_filters
from django_filters import CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Q
from .models import Post
from .serializers import PostSerializer

class CustomPostFilterSet(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

class CustomFilterBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)
        param_value = request.query_params.get('title')
        if param_value:
            kwargs['queryset'] = CustomPostFilterSet(data={'title': param_value}, queryset=queryset).qs
        return kwargs

class PostApiViewPagination(PageNumberPagination):
    page_size = 5;
    page_query_param = 'page size';
    max_page_size = 10000;


class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostApiViewPagination
    filter_backends = [CustomFilterBackend]

    @action(detail=False, methods=['get'], url_path='custom_filter')
    def custom_filter(self, request):
        queryset = Post.objects.filter(
            Q(title__icontains='футбол') & ~Q(description__lte=10) | Q(author='sport-express')
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_post(self, request, pk):
        post = self.get_object()
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


