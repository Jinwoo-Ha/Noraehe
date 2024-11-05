from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loading/', views.loading, name='loading'),
    path('analyze/', views.analyze, name='analyze'),
    path('recommend/', views.recommend, name='recommend'),
    path('mypage/', views.mypage, name='mypage'),  # 새로 추가된 경로
    path('search_song/', views.search_song, name='search_song'),

]
