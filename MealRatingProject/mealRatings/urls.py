from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('category/<int:meal_time>/', views.category_list, name='category_list'),
    path('meal/<int:meal_id>/', views.meal_detail, name='meal_detail'),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('rate_meal/<int:meal_id>/', views.rate_meal, name='rate_meal'),
]
