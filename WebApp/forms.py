from django import forms
from WebApp.models import Registationproject

class Registationproject(forms.ModelForm):
    firstname=forms.CharField(max_length=15,label="Firstname")
    lastname=forms.CharField(max_length=15,label="Lastname")
    email=forms.EmailField(required=True)
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
    password1=forms.CharField(widget=forms.PasswordInput,label="PasswordConfirmation")
    class Meta:
        model=Registationproject
        fields="__all__"
