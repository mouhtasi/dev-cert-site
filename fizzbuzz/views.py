from django.shortcuts import render
from .models import Topic


def index(request):
    topics = Topic.objects.all()
    return render(request, 'fizzbuzz/index.html', {'topics': topics})
