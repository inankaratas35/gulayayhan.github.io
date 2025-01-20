from django.urls import path
from .views import HomeView, RecipeDetailView, about_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('about/', about_view, name='about'),
]