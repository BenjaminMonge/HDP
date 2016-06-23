from django.conf.urls import url

from . import views

#the equivalent of the angular router, according to a url gives a template and controller
#ngRouter's routeProvider
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^management/$', views.management, name='management'),
	url(r'^see/$', views.see, name='see'),
	url(r'^editeq/$', views.editeq, name='editeq'),
	url(r'^extrapolate/$', views.extrapolate, name='extrapolate'),
	url(r'^extrapolate/getdata$', views.getData, name='data'),

]
