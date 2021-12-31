from django.urls import path
from why.views import whyus


app_name = "why"

urlpatterns = [
    path('', whyus, name="whyus")
]