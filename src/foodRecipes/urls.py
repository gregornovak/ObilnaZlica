from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.zadnji_recepti, name="zadnji_recepti"),
    url(r'^recepti$', views.vsi_recepti, name="vsi_recepti"),
    url(r'^recept/(?P<id>\d+)/$', views.posamezen_recept, name='posamezen_recept'),
    #url(r'^recepti/(?P<id>\w)$', views.kategorija_recepta, name="kategorija_recepta"),
]
