from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lesson/(?P<topic_name>\w+)/$', views.lesson, name='lesson'),
    url(r'^test/(?P<topic_name>\w+)/$', views.test, name='test'),
    url(r'^guest_certificate/(?P<topic_name>\w+)/$', views.get_guest_certificate, name='get_guest_certificate'),
    url(r'^certificate/(?P<topic_name>\w+)/$', views.certificate, name='certificate'),
]
