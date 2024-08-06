from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit
import os

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)



def about_view(request, *args, **kwargs):
    name = os.getenv("NAME", "no name given")
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = round(page_qs.count() / qs.count() * 100.0,1)
    except ZeroDivisionError:
        percent = 0
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
        "name": name,    
    }
    path = request.path
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)