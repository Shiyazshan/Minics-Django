from django.shortcuts import render
from why.models import WhyUs

def whyus(request):
    whyuss = WhyUs.objects.all()

    context = {
        'whyuss' : whyuss
    }

    return render(request,"why.html", context = context)