from django.urls import path
from user.views import about,user_login


app_name = "user"

urlpatterns = [
    path('about/', about, name="about"),
    path("",user_login,name="user_login"), 
]