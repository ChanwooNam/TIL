from django.urls import path 
from . import views

urlpatterns = [

    # config/ urls.py에서 잘라왔다 
    path('static_sample/', views.static_sample),

    path('user_create/', views.user_create),
    path('user_new/', views.user_new),

    path('result/' ,views.result),
    path('art/' ,views.art),

    path('catch/', views.catch),
    path('throw/', views.throw),

    # '/'경로로 들어왔을 때 index 페이지
    # 기본적으로 앞에 / 가 붙어있어서 별도로 '/'를 붙여주지 않아도 된다 
    path('', views.index),  

]
