from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	nickname = forms.CharField()

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise ValidationError("Username taken")
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError("Email used")
		return email
		