
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('news_list/', views.news_list, name='news_list'),
    path('account/', views.account, name='account'),
    path('sidebar/', views.sidebar, name ='sidebar'),
    path('no_page_error/', views.no_page_error, name ='no_page_error'),
]
