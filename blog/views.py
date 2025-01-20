from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe, About

class HomeView(ListView):
    model = Recipe
    template_name = 'blog/home.html'
    context_object_name = 'recipes'
    paginate_by = 6

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'blog/recipe_detail.html'

def about_view(request):
    about = About.objects.first()
    return render(request, 'blog/about.html', {'about': about})