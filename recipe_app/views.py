from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_app/home.html', context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name="recipe_app/home.html"
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'recipe_app/about.html', {'title': 'About'})