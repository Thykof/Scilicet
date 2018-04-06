# Create your forms here.

from django.utils.translation import gettext_lazy as _
from django import forms


from candidate.models import Profile, Item


class SigninForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password_nd = forms.CharField(label="Encore", widget=forms.PasswordInput)
    email = forms.EmailField(label="Adresse mail")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Adresse mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class ModifyProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
        labels = {
            'bio': _('Bio'),
            'location': _('Localisation'),
            'birth_date': _('Date de naissance'),
        }

class ModifyUser(forms.Form):
    email = forms.EmailField(label="Adresse mail")

class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['subitem']
