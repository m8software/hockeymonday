from django.shortcuts import render
from Statistics.models import *
from django.http import Http404
def home_page(request):
    try:
        players = Player.objects.all()
    except Player.DoesNotExist:
        raise Http404("Poll does not exist")
    context = {
        "players" : players
    }
    return render(request, "home.html", context)