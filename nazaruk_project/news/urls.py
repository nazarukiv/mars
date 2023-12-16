from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from .views import NewsUpdateView

urlpatterns = [
    path('create', views.create, name='create'),
    path('news/category/<str:category>/', views.news_home, name='news_category'),
    path("<int:pk>", views.NewsDetailView.as_view(), name='news-detail'),
    path('news/update/<int:pk>/', views.NewsUpdateView.as_view(), name='news-update'),
    path("<int:pk>/delete", views.NewsDeleteView.as_view(), name='news-delete'),
    path('', views.news_home, name='news_home'),
    # Removing the problematic URL
    # path('news/', NewsUpdateView.as_view(), name='news_home'),
]

