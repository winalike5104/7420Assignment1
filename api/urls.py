
from django.urls import path
from .views import article_list,article_detail
from .frontend import log_in

urlpatterns = [
    
    path('article/',article_list ),
    path('detail/<int:pk>/',article_detail ),
    path('',log_in)
]
