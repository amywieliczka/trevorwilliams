# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from common.models import Navigation

def home(request):
    n = Navigation.objects.all().order_by('order')
    context = {'navs': n}
    return render(request, 'common/home.html', context)

def page(request, slug):
    n = Navigation.objects.all().order_by('order')
    p = Navigation.objects.get(slug=slug)
    context = {'page': p, 'navs': n}
    return render(request, 'common/content.html', context)