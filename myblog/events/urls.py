from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventView.as_view()),
    path('<int:pk>/', views.EventDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='event_add_comments'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='event_add_likes'),
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='event_del_likes'),
    path('api/eventlist', views.EventListCreateAPIView.as_view())
]