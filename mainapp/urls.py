from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^personal_development', views.personal_development, name='personal development'),
    url(r'^presentation$', views.presentation, name='presentation'),
    url(r'^design_report$', views.design_report, name='design report'),
    url(r'^blog$', views.blog, name='blog'),
]
