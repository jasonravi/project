from django.conf.urls import patterns, include, url

from django.contrib import admin
from ravi.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(?P<user_id>\d+)/$', name_of_permission,
        name="name_of_permission"),
    url(r'^checkpermission1/$', check_user_permission,
        name="check_user_permission"),
    url(r'^roles/(?P<role_id>\d+)/$', modify_permission,
        name="modify_permission"),
    url(r'^delete_permission/(?P<permission_id>\d+)/$', delete_permission,
        name="delete_permission"),

)
