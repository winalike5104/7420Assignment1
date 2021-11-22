from django.urls import path
from django.conf.urls import url
from .views import *



urlpatterns = [
    
    path('dogInfo_list/',dogInfo_list ),
    # url(r"^(?P<slug>[\w-]+)/$",dog_detail,name="detail"),
    path('appointment_detail/<slug>/<judge>',appointment_detail,name = "detail1"),
    path('dog_detail/<slug>/<judge>',dog_detail,name="detail"),
    
    path('dog_post/',dog_post,name="post"),
    path('appointments/',appointments),
    path('setAappointment/',setAappointment),
    path('book/<id>',book),
    path('quit/<id>',quit),
    
    path('editdog/<id>',editdog)
]