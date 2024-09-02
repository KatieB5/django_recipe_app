from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipe_app/home.html')

def about(request):
    return render(request, 'recipe_app/about.html')