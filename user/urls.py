from django.urls import path
from user.views import about


app_name = "user"

urlpatterns = [
    path('', about, name="about"),
]