# Create your forms here.

from django import forms


from candidate.models import Profile


class SigninForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password_nd = forms.CharField(label="Encore", widget=forms.PasswordInput)
    email = forms.EmailField(label="Adresse mail")

class LoginForm(forms.Form):
    last_name = forms.CharField(label="Nom", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
