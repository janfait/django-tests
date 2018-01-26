"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
    
When somebody requests a page from your Web site say, /polls/34/, Django will load the mysite.urls Python module because its pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the regular expressions in order. The include() functions we are using simply reference other URLconfs. Note that the regular expressions for the include() functions don???t have a $ (end-of-string match character) but rather a trailing slash. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under ???/polls/???, or under ???/fun_polls/???, or under /content/polls/, or any other path root, and the app will still work.
Heres what happens if a user goes to /polls/34/ in this system: 
  Django will find the match at '^polls/'
  Then, Django will strip off the matching text ("polls/") and send the remaining text "34/" to the polls.urlsURLconf for further processing which matches r'^(?P<question_id>[0-9]+)/$' resulting in a call to the detail() view like so:
  detail(request=<HttpRequest object>, question_id='34')    
    
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

"""
url() argument: view
When Django finds a regular expression match, Django calls the specified view function, with an HttpRequest object as the first argument and any ???captured??? values from the regular expression as other arguments. If the regex uses simple captures, values are passed as positional arguments; if it uses named captures, values are passed as keyword arguments. We'll give an example of this in a bit.
url() argument: kwargs
Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren???t going to use this feature of Django in the tutorial.
url() argument: name
Naming your URL lets you refer to it unambiguously from elsewhere in Django especially templates. This powerful feature allows you to make global changes to the url patterns of your project while only touching a single file.
"""
urlpatterns = [
    url(r'^', include('snippets.urls',namespace="snippets")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]





