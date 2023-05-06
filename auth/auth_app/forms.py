from django import forms
from django.contrib.auth.models import User
from auth_app.models import UserProfileInfo
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput) # overwriting it to be hidden
    class Meta():
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio','picture')
