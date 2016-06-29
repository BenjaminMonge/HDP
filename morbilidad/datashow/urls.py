from django.conf.urls import url, patterns
from django.contrib import admin
from . import views

#the equivalent of the angular router, according to a url gives a template and controller
#ngRouter's routeProvider
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^management/$', views.management, name='management'),
	url(r'^see/$', views.see, name='see'),
	url(r'^extrapolate/$', views.extrapolate, name='extrapolate'),
    url(r'^editeq/$', admin.site.admin_view(views.editeq)),

]



