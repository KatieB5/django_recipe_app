from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='create'),
    path('about/', views.about, name='about'),
]