from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Topic

# Create your views here.
def index(response):
    return HttpResponse("Okay this is working now")

class IndexView(generic.ListView):
    model = Topic
    template_name = 'topics/index.html'
    context_object_name = 'list_of_topics'

    def get_queryset(self):
        return Topic.objects.all()
