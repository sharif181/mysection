from django.urls import path
from . import views
urlpatterns = [
    path('saturday', views.saturday, name="saturday"),
    path('sunday', views.sunday, name="sunday"),
    path('monday', views.monday, name="monday"),
    path('tuesday', views.tuesday, name="tuesday"),
    path('wednesday', views.wednesday, name="wednesday"),
    path('thursday', views.thrusday, name="thrusday"),
    path('extra', views.extra, name="extra"),
    
    

]







