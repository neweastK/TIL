from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('<int:article_pk>/comments/', views.create_comment),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    path('event/', views.event_list_or_create),
    path('news/', views.news_list_or_create),
    path('column/', views.column_list_or_create),
    path('board/', views.board_list_or_create),
    path('sinye/', views.sinye_list_or_create),

]

