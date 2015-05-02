from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Return hello world response."""
    return HttpResponse("Hello, world. You're at the polls index.")
