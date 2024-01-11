from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .viewsets import PostListViewSet

router = DefaultRouter()
router.register(r'posts', PostListViewSet, basename='post')

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/posts', views.PostListCreateAPIView.as_view()),
    path('api/posts/<int:pk>/add_likes/', views.LikeApiAdd.as_view()),
    path('api/posts/<int:pk>/del_likes/', views.LikeApiDel.as_view()),
    path('api/', include(router.urls)),
]