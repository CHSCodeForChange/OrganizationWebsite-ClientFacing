from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.form, name='form'),
    url(r'^organization/$', views.organization, name='organization'),
    url(r'^media/$', views.media, name='media'),
    url(r'^school/$', views.school, name='school'),
    url(r'^other/', views.other, name='other'),
]
