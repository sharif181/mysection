from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('quiz',views.Quiz, name="quiz"),
    path('presentation',views.Presentation, name="presentation"),
    path('assignment',views.Assignment,name="assignment"),
    path('routine',views.routine,name="routine"),
   
]