from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from riskapi import views


urlpatterns = [
    url(r'^riskapi/v1/users/$', views.UserList.as_view()),
    url(r'^riskapi/v1/users/(?P<pk>[0-9]+)/$', views.UserList.as_view()),    
    url(r'^riskapi/v1/risktypekeys/$', views.RiskTypeKeyList.as_view()),
    url(r'^riskapi/v1/riskkeys/$', views.RiskKeyList.as_view()),    
    url(r'^riskapi/v1/risktypes/$', views.RiskTypeList.as_view()),
    url(r'^riskapi/v1/risktypedetail/(?P<pk>[0-9]+)/$', views.RiskTypeDetail.as_view()),
    url(r'^riskapi/v1/risks/$', views.RiskList.as_view()),
    url(r'^riskapi/v1/riskdetail/(?P<pk>[0-9]+)/$', views.RiskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)