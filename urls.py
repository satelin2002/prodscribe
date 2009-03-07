from django.conf.urls.defaults import *
from accounts.views import register
# Uncomment the next two lines to enable the admin:
# ADMIN.
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^prodscribe/', include('prodscribe.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^register$', register),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
