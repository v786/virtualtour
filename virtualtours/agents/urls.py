from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('login/', views.login_try, name='login_try'),
    path('signin/', views.signin, name ='signin'),
]