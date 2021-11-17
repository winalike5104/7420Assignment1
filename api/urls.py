
from django.urls import path
from .views import loginInfo_list,loginInfo_detail
from .frontend import *

urlpatterns = [
    
    path('loginInfo/',loginInfo_list ),
    path('detail/<int:pk>/',loginInfo_detail ),
    path('login_rest',log_in),
    path('registerPage/',jump_to_register_page),
    path('indexPage/',jump_to_index),
]
