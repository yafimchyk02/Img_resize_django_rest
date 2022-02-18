from django.urls import path
from resize_IMG import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home')
] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
