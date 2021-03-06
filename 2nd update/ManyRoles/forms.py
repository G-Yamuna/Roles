from django import forms
from ManyRoles.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
	password1 =forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"password"}))
	password2 =forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"confirm password"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"username"
			})
		}
