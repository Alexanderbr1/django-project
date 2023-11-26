from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api/postlist', views.PostApiView.as_view()),
]