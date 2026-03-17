# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings        # обязательно
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analyzer.urls')),  # подключение приложения analyzer
]

# Раздача статических файлов во время разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
