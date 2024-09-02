from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_app/home.html', context)

def about(request):
    return render(request, 'recipe_app/about.html', {'title': 'About'})