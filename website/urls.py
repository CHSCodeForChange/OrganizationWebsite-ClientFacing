from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^team/', views.team, name='team'),
    url(r'^map/', views.map, name='map'),
    url(r'^activity/', views.activity, name='activity'),
    url(r'^contact/', views.contact),
    url(r'^keepalive/', views.keepalive, name='keepalive'),
]
