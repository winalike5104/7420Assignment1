from django.urls import path
from django.conf.urls import url
from .views import dog_detail,dogInfo_list,dog_post



urlpatterns = [
    
    path('dogInfo_list/',dogInfo_list ),
    # url(r"^(?P<slug>[\w-]+)/$",dog_detail,name="detail"),
    path('dog_detail/<slug>',dog_detail,name="detail"),
    path('dog_post/',dog_post,name="post")
]