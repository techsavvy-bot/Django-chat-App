from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginPage, name="loginPage"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('createRoom', views.createRoom, name="createRoom"),
    path('signup', views.signup, name="signup"),
    path('<str:room_name>/', views.room, name='room')
]
