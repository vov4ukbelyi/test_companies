from django.conf.urls import url

from . import views

app_name = 'company'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.AddView.as_view(), name='company_add'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='company_detail'),
    url(r'^detail/(?P<pk>[0-9]+)/edit/$', views.CompanyEdit.as_view(), name='company_edit'),
    url(r'^detail/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company_delete')
]