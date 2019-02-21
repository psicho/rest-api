from django.conf.urls import url
from api import api

urlpatterns = (
    # url(r'^$', views.App.as_view(), name='index'),
    url(r'categories1/$', api.TopModelList.as_view(), name='topmodellist'),
    url(r'/categories1/(?P<pk>\d+)$', api.TopModelDetails.as_view(), name='topmodeldetail'),
    url(r'categories/$', api.ModelsList.as_view(), name='modellist'),
    url(r'/categories/(?P<pk>\d+)$', api.ModelsDetails.as_view(), name='modeldetail'),
)
