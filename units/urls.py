from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
	
        url(r'^gundam/$',views.gundamlist.as_view(), name = 'gundam_list'),
	url(r'^gundam/(?P<pk>[0-9]+)/$',views.gundamdetail.as_view(), name = 'gundam_detail'),
	url(r'^pilot/$',views.pilotlist.as_view(), name = 'pilot_list'),
	url(r'^pilot/(?P<pk>[0-9]+)/$',views.pilotdetail.as_view(), name = 'pilot_detail'),
	url(r'^weapon/$',views.weaponlist.as_view(), name = 'weapon_list'),
	url(r'^weapon/(?P<pk>[0-9]+)/$',views.weapondetail.as_view(), name = 'weapon_detail'),
	url(r'^utils/$',views.utilslist.as_view(), name = 'utils_list'),
	url(r'^utils/(?P<pk>[0-9]+)/$',views.utilsdetail.as_view(), name = 'utils_detail'),
]
