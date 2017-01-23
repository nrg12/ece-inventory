from django.conf.urls import url

from . import views

#this app_name is important b/c Django needs to look through all the apps 
# and we need to differentiate
app_name = 'inventory'  
urlpatterns = [
    # the argument 'name' at the end of url() is IMPORTANT 
    # b/c we use it to load these urls later in the html files
    # this allows us to change the url of a page without changing it in the HTML files
    
    # this is what it goes to if typed /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # to post a new request
    url(r'^post/request/$', views.post_new_request, name='post_new_request'),

]