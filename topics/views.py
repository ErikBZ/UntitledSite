from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth import authenticate, login

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

'''
    Intstead of it being a ListView it need to be a DetailView
    Maybe because DetailViews are smart about picking up which
    object it needs and naming it accordingly. In this case it is called "topic"
'''
class TopicDetailedView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic_detail.html'

def detail(request, topic_id):
    top = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'topics/topic_detail.html', {'topic':top})

def user_login(request):
    template_name = 'topics/login.html'
    return render(request, template_name)