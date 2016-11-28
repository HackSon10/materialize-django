from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^comment/(?P<persona_id>[\w]+)/', views.comments),
    url(r'^noti/$', views.noti, name="noti"),
    url(r'^chat/$', views.chat, name="chat"),
    url(r'^user/$', views.prefile, name="profile"),
    url(r'^vcall/$', views.vcall, name="vcall"),
    url(r'^help/$', views.helpme, name="help"),
    url(r'^register/$', views.register, name="register"),
]
