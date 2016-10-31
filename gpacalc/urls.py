from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^home/', views.home, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^editcollege/', views.editcollege, name='editcollege'),
    url(r'^editprofile/', views.editprofile, name='editprofile'),
    url(r'^editfuture/', views.editfuture, name='editfuture'),
    url(r'^currentclasses/', views.currentclasses, name='currentclasses'),
    url(r'^class/', views.currentclass, name='class')
]