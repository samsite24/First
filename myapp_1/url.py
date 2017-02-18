# February 09, 2017
# @samsite

from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'func/', views.func, name='func'),
    url(r'^problem/(?P<pk>\d+)/', views.problems, name='problems'),
)
