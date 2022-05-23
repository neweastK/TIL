from django.urls import path
from . import views

urlpatterns = [
    # 영화 리스트를 가져올 때, view에서 추천 로직을 짜는가 vue에서 짜는가
    path('', views.movie_list),
    path('boxoffice/', views.boxoffice_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:person_pk>/person/', views.person_detail),
    path('<int:movie_id>/review/', views.review_create),
    path('<int:movie_id>/review/<int:review_pk>/', views.review_update_or_delete),
]
