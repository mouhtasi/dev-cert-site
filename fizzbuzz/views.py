from django.shortcuts import render


def index(request):
    return render(request, 'fizzbuzz/index.html')
