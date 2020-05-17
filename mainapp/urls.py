from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^personal_development', views.personal_development, name='personal development'),
    url(r'^presentation$', views.presentation, name='presentation'),
    url(r'^design_report$', views.design_report, name='design report'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^indus$', views.indus, name='indus'),
    url(r'^bauhaus$', views.bauhaus, name='bauhaus'),
    url(r'^newtyp$', views.newtyp, name='newtyp'),
    url(r'^newyork$', views.newyork, name='newyork'),
    url(r'^russia$', views.russia, name='russia'),
    url(r'^psa$', views.psa, name='psa'),
    url(r'^roles$', views.roles, name='roles'),
    url(r'^diary$', views.diary, name='diary'),
]
