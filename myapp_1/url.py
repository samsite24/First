# February 09, 2017
# @samsite

from django.conf.urls import url
from myapp_1 import views

urlpatterns = (
    url(r'func/', views.func, name='func'),
)
