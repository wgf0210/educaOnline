from django.urls import path
from . import views
from .views import *


user_list = UserProfileViewSet.as_view({'get':'list'})
user_detail = UserProfileViewSet.as_view({'get':'retrieve','delete':'destroy'})

ulpatterns = [
    path('',views.api_root),
    path('users/',user_list,name='user-list'),
    path('users/(?P<pk>[0-9]+)/',user_detail,name='user-detail'),

]