from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # articles/ 로 요청했을 경우 index 함수 실행
    
    path('', views.index, name='index'),   # READ Logic - Index
    # path('new/', views.new, name='new'),    # CREATE Logic - 폼 전달
    path('create/', views.create, name='create'),  # CREATE Logic - DB에 저장
    path('<int:article_pk>/', views.detail, name='detail'),  # READ Logic - Detail
    path('<int:article_pk>/delete/', views.delete, name='delete'),   # DELETE Logic
    path('<int:article_pk>/update/', views.update, name='update'),   # UPDATE Logic - DB 저장
    
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    #path('<int:article_pk>/edit/', views.edit, name='edit'),    # UPDATE Logic - 폼 전달
    
    path('<int:article_pk>/like', views.like, name='like'),

    path('<int:article_pk>/follow/<int:user_pk>', views.follow, name='follow'),

    path('list/', views.list, name='list'),
    path('explore/', views.explore, name='explore'),

]
