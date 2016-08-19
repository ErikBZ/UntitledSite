from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

from .models import Topic

# Create your views here.
def index(response):
    return HttpResponse("Okay this is working now")

class IndexView(generic.ListView):
    model = Topic
    template_name = 'topics/homepage.html'
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

class UserProfileView(generic.DetailView):
    model = User


'''
    Oh shit this works
'''
@login_required
def submit_post(request):
    template_name = 'topics/submit_post_form.html'

    model = Topic
    context = {
        'model':Topic,
    }

    topic_text = ''
    description_text = ''
    pub_date = ''
    number_of_replies = 0
    user_who_posted = ''

    if request.POST:
        topic_text = request.POST['title']
        description_text = request.POST['desc']
        pub_date = datetime.datetime.now()
        user_who_posted = request.user
        new_topic = Topic.objects.create(topic_text=topic_text,
            description_text=description_text, pub_date=pub_date,
            user_who_posted=user_who_posted, number_of_replies=number_of_replies)
        print(description_text)
        return HttpResponseRedirect('/topics/{}'.format(new_topic.id))

    return render(request, template_name, context)

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

def register_user(request):
    template_name = 'topics/register_user.html'
    if request.POST:
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username, email, password)
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
