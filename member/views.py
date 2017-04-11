from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import SignupForm
from .models import Member, PaymentMethod

def signup(request):
	if request.method == 'GET':
		return render(request, 'member/signup.html', {'form': SignupForm()})
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
			login(request, user)
			member = Member.create(user=user, nickname=form.cleaned_data['nickname'])
			PaymentMethod.create(account_number=user.id, member=member)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'member/signup.html', {'form': form})
