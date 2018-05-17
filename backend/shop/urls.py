from django.urls import path, include
from . import views

api = [
    path('categories/', views.CategoriesView.as_view()),
    path('category/<category_name>/', views.CategoryView.as_view()),
    path('click_product/', views.ClickProductView.as_view()),
    path('product/<int:_id>/', views.ProductView.as_view()),
]

urlpatterns = [
    path('', views.SPAView.as_view()),
    path('api/', include(api))
]
