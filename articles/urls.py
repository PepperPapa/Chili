from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/edit', views.edit, name="edit"),
]