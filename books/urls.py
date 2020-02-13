# from django.contrib import admin
from django.urls import path
from books import views
app_name = 'books'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:i_id>', views.detail, name='detail')
]
