from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.view import hello,current_datetime,hours_ahead
from mysite.books import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^search/$', views.search),
)
