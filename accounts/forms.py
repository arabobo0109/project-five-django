from django import forms

class UserLoginForm(forms.Form):
    """Form for users to log in"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)