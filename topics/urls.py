from django.conf.urls import url
from . import views

app_name = 'topics'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.TopicDetailedView.as_view(),
        name='one_topic'),
    url(r'^submit/', views.submit_post, name='submit_post')
]
