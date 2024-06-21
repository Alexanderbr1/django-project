from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myblog.views import redirect_to_news

urlpatterns = [
    path('', redirect_to_news),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('events/', include('events.urls')),
    path('accounts/', include('accounts.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)