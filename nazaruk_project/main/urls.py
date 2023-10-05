from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about', views.about, name='about'),
    path('ivan', views.ivan),
    path('index', views.index, name='home'),
    path('contact_us', views.contact, name='contact')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)