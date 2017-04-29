from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import ModelBackend

from .forms import SignupForm
from .models import Member, PaymentMethod

def signup(request):
	if request.method == 'GET':
		return render(request, 'member/signup.html', {'form': SignupForm()})
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user:
				login(request, user)
				member = Member.create(user=user, nickname=form.cleaned_data['nickname'])
				PaymentMethod.create(account_number=user.id, member=member)
				return HttpResponseRedirect('/')
			return render(request, 'member/signup.html', {'form': form})
		else:
			return render(request, 'member/signup.html', {'form': form})

def purchased_games(request):
    if not request.user.is_authenticated():
        return HttpResponse('Please log in or sign up first')
    member = request.user.member
    PurchaseRecords = member.get_purchase_history().all()
    games = []
    for record in PurchaseRecords:
        if record.item.game not in games:
            games.append(record.item.game)
    context = {'games': games, 'len': len(games)}
    return render(request, 'member/purchased.html', context)
