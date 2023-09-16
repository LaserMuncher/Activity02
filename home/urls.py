from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
            static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)