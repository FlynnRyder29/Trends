from django import forms
class loginForm(forms.Form):
    user=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
