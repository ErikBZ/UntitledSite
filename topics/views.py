from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from .models import Topic

# Create your views here.
def index(response):
    return HttpResponse("Okay this is working now")

class IndexView(generic.ListView):
    model = Topic
    template_name = 'topics/index.html'
    context_object_name = 'list_of_topics'

    '''
    def get_queryset(self):
        return Topic.objects.all()
    '''

    '''
        it seems that user is also defined as a context object
        i'm not setting it here and i can still use it in index.html
    '''
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

'''
    Intstead of it being a ListView it need to be a DetailView
    Maybe because DetailViews are smart about picking up which
    object it needs and naming it accordingly. In this case it is called "topic"
'''
class TopicDetailedView(generic.DetailView):
    model = Topic
    template_name = 'topics/topic_detail.html'

'''
    basic login view, i just need to fix up the css for the login page
    so it doesn't look like ass
'''
def user_login(request):

    template_name = 'topics/login.html'
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/topics/')

    return render(request, template_name)

def user_logout(request):
    template_name = 'topics/logout.html'
    logout(request)
    return(HttpResponseRedirect('/topics/'))
