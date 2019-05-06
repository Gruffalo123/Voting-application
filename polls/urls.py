from django.urls import path
from polls import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('index/',views.index,name='index'),# 二级路由 polls/index
]