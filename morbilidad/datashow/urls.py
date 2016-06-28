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

]

def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^editeq/$', admin.site.admin_view(views.editeq))
        )
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls

