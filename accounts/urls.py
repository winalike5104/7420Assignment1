from django.urls import path
from .views import signup_view,login_view,logout_view,sendEmail,check,reset

urlpatterns = [
    
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('email/',sendEmail),
    path('check/',check),
    path('reset/',reset)
    
]