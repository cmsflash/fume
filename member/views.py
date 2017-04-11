from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SignupForm

def signup(request):
	if request.method == 'GET':
		return render(request, 'member/signup.html', {'form': SignupForm()})
