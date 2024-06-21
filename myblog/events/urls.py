from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.EventView.as_view()),
    path('<int:pk>/', views.EventDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='event_add_comments'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='event_add_likes'),
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='event_del_likes'),
    path('api/eventlist', views.EventListCreateAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]