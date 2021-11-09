
from django.urls import path
from .views import loginInfo_list,loginInfo_detail
from .frontend import log_in

urlpatterns = [
    
    path('loginInfo/',loginInfo_list ),
    path('detail/<int:pk>/',loginInfo_detail ),
    path('',log_in)
]
