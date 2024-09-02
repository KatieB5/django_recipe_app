from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.

def register(request):
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"An account for {username} has been created! Please log in.")
            return redirect('login_user')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')