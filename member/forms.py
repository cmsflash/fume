from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
	username: forms.CharField = forms.CharField()
	password: forms.CharField = forms.CharField(widget=forms.PasswordInput)
	email: forms.EmailField = forms.EmailField()
	nickname: forms.CharField = forms.CharField()

	def clean_username(self) -> str:
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise ValidationError("Username taken")
		return username

	def clean_email(self) -> str:
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError("Email used")
		return email
		