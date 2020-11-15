from django.shortcuts import redirect
from django.shortcuts import render


def home(request):

	return render(request, 'mechanizm/home.html')

def profile(request):

	return render(request, 'mechanizm/profile.html')
