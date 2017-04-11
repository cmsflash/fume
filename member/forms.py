from django import forms

class SignupForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	nickname = forms.CharField()