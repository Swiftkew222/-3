from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Домашняя страница 
    path('', views.home, name='home'),  

    # Новости
    path('news/', views.news_list, name='news_list'),  # список новостей
    path('news/<int:pk>/', views.news_detail, name='news_detail'), # подробный пост
    path('news/add/', views.add_news, name='add_news'),
    
    # Контакты
    path('contacts/', views.contacts, name='contacts'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
]
