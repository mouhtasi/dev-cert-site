from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lesson/(?P<topic>\w+)/$', views.lesson, name='lesson'),
]
