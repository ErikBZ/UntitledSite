"""untitled_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^topics/', include('topics.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', 'topics.views.user_login', name="user_login"),
]

'''
    apparently i needed to have name='name' instead of just a string
    also it seems like it's best to put this in my topics apps folder instead
    url(r'^login/', views.login_default, name='login_default' ),
    Even though the login view is not in the root folder i can still do this
    so that i don't have a /topics/login situtation instead its just login
    woo hoo
'''
