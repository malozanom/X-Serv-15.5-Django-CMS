from django.conf.urls import include, url
from django.contrib import admin
from cms import views

urlpatterns = [
    url(r'^cms/?$', views.show, name='Show the dictionary content'),
    url(r'^cms/(1|2)$', views.entry, name='Selected page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'.*', views.error, name='Not found in dictionary')
]
