# core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html')
  
def signupuser(request):
	if request.method == 'GET':
		return render(request, 'signupuser.html', {'form': UserCreationForm})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('home')
			except IntegrityError:
				return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Username already taken Plese choose different username'})
		else:
			return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Password did not match.'})
