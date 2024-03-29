import django_filters
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event, EventLikes
from .form import CommentsForm
from .serializers import EventSerializer


class EventView(View):
    '''Вывод записей'''
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'events/events.html', {'event_list': events})

# Create your views here.
class EventDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        event = Event.objects.get(id=pk)
        sports = event.sports.all()
        context = {
            'event': event,
            'sports': sports
        }
        return render(request, 'events/event_detail.html', context)

class AddComments(View):
    '''Добавление комментариев'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.event_id = pk
            form.save()
        return redirect(f'/events/{pk}')

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
            EventLikes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/events/{pk}')
        except:
            new_like = EventLikes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/events/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = EventLikes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/events/{pk}')
        except:
            return redirect(f'/events/{pk}')



class EventApiViewPagination(PageNumberPagination):
    page_size = 3;
    page_query_param = 'page size';
    max_page_size = 10000;

class EventListCreateAPIView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = EventApiViewPagination
    filter_backends = [SearchFilter]
    search_fields = ['date', 'description']

    @action(detail=False, methods=['get'], url_path='custom_filter')
    def custom_filter(self, request):
        queryset = Event.objects.filter(
            Q(date__gt='2022-01-01') & (Q(description__icontains='спорт') | Q(description__icontains='музыка')) & ~Q(
                location='стадион')
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


