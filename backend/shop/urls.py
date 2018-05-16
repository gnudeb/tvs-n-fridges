from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('category/<category_name>/', views.CategoryView.as_view()),
    path('click_product/', views.ClickProductView.as_view()),
]
