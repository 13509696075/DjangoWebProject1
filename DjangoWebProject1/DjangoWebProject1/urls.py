"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.urls import path
from DjangoWebProject1 import views
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebProject1.views.home, name='home'),
    # url(r'^DjangoWebProject1/', include('DjangoWebProject1.DjangoWebProject1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('gogo/',views.pylinkweb),
    path('fv/',views.deposits),
    path('result/',views.result),
]
