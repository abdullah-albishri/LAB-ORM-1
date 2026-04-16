from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('post/', views.post_view, name='post_view'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]