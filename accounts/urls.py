from django.urls import path
from . import views

urlpatterns = [path('login/', views.login, name='login'),
               path('', views.login, name='login'),
               path('sair/', views.sair, name='sair'),
               path('cadastro/', views.cadastro, name='cadastro'),
               path('dashboard/', views.dashboard, name='dashboard')]
