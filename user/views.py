from django.shortcuts import render
from user.models import About


def about(request):
    abouts = About.objects.all()

    context = {
        'abouts' : abouts,
    }

    return render(request, "about.html", context=context)


