from django.shortcuts import render, HttpResponse

#Dummy data
recipes = [
    {
        'author': 'Adam',
        'title': 'Baked Oat Bars',
        'directions': 'Throw all ingredients into a bowl and stir to combine, then bake.',
        'date_posted': 'May 19, 2024'
    },
    {
        'author': 'Benji',
        'title': 'Carbonara',
        'directions': 'Throw all ingredients into a pan, hope for the best.',
        'date_posted': 'June 19, 2024'
    },
    {
        'author': 'Carla',
        'title': 'Double chocolate fudge cake',
        'directions': 'Mix ingredients, bake for 40 mins then eat the whole thing.',
        'date_posted': 'July 19, 2024'
    },
]

# Create your views here.
def home(request):
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_app/home.html', context)

def about(request):
    return render(request, 'recipe_app/about.html', {'title': 'About'})