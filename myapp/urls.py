from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loading/', views.loading, name='loading'),
    path('analyze/', views.analyze, name='analyze'),
    path('recommend/', views.recommend, name='recommend'),
]
