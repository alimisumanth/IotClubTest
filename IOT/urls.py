from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    url(r'^$', views.homepage, name='index'),
    url(r'^workshops/$', views.workshops, name='workshops'),
    url(r'^course/$', views.course, name='course'),
    url(r'^achievements/$', views.achievements, name='achievements'),
    url(r'^corebody/$', views.corebody, name='corebody'),
    url(r'^index/$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='Projects'),
]
urlpatterns += staticfiles_urlpatterns()
