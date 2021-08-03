from django.contrib import admin
from django.urls import path, include
from tst import views


urlpatterns = [
    path('index/', views.index),
    path('scheduler/', views.schedul),
    path('cancell/', views.cancell),
    path('clear/', views.clear_sessions_command),
    # path('task/', views.task),

]
