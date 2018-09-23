from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('login/', views.login_try, name='login_try'),
    path('logout/', views.signout, name ='signout'),
    path('signin/', views.signin, name ='signin'),
    path('register/', views.register_user, name ='register_user'),
]