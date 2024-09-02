from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the recipes app!")

def about(request):
    return HttpResponse("This is a recipes app to keep track of your recipes.")