from django.urls import path
from web.models import Testimonial
from web.views import index,subscribe,testimonial


app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("subscribe/", subscribe, name="subscribe"),
    path("testimonial/",testimonial,name= "testimonial"),

]