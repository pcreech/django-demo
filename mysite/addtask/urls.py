from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/(?P<left>[0-9]+)/(?P<right>[0-9]+)/', views.add, name='add')
]
