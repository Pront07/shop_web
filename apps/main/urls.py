from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('articles/', views.articles, name='articles'),
    path('about/', views.about, name='about'),

]

