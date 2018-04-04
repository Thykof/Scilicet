from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from candidate.forms import SigninForm, LoginForm, ModifyProfile, ModifyUser
from candidate.models import Profile


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                return redirect(reverse('candidate:home'))
            else:
                error = 'Nope, l\'authentification a échoué :/'

                return render(request, "candidate/login.html", locals())

        else:  # invalid form
            error = 'Nope, le formulaire n\'est pas valide :/'
            return render(request, "candidate/login.html", locals())

    else:
        if request.user.is_authenticated:
            return redirect(reverse('candidate:home'))
        else:
            form = LoginForm()
            return render(request, "candidate/login.html", locals())

def signin_view(request):
    error = ''
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            password_nd = form.cleaned_data["password_nd"]
            email = form.cleaned_data["email"]

            for user in User.objects.all():
                if user.email == email or user.username == last_name:
                    error = 'Nope, cette adresse mail est déjà utilisée (*) :/'
                    # It can be caused by email OR last name
                    # because last name is used to login
                    return render(request, 'candidate/signin.html', locals())

            if password == password_nd:
                user = User.objects.create_user(last_name, email, password,
                                                first_name=first_name,
                                                last_name=last_name,
                )
                profile = Profile(user=user)
                profile.save()

                user = authenticate(username=email, password=password)
                login(request, user)

                return redirect(reverse('candidate:home'))

            else:
                error = 'Nope, les deux mots de passe ne sont pas identiques :/'

        else:  # invalid form
            error = 'Nope, le formulaire n\'est pas valide :/'

    else:  # method = GET
        form = SigninForm()

    return render(request, 'candidate/signin.html', locals())

@login_required
def home_view(request):
    return render(request, 'candidate/home.html', locals())

@login_required
def profile_view(request):
    return render(request, 'candidate/profile.html', locals())

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

@login_required
def fill_view(request):
    error = ''
    if request.method == 'POST':
        form = ModifyProfile(request.POST)
        if form.is_valid():
            request.user.profile.bio = form.cleaned_data['bio']
            request.user.profile.location = form.cleaned_data['location']
            request.user.profile.birth_date = form.cleaned_data['birth_date']
            request.user.profile.save()
            return redirect(reverse('candidate:home'))
        else:
            error = 'Nope, il y a une erreur dans le formulaire.'
    else:
        form = ModifyProfile()
    return render(request, 'candidate/fill.html', locals())

@login_required
def fill_user_view(request):
    error = ''
    if request.method == 'POST':
        form = ModifyUser(request.POST)
        if form.is_valid():
            print(request.user.email)
            print(form.cleaned_data['email'])
            request.user.email = form.cleaned_data['email']
            request.user.save()
            print(request.user.email)
            return redirect(reverse('candidate:home'))
        else:
            error = 'Nope, il y a une erreur dans le formulaire.'
    else:
        form = ModifyUser()
    return render(request, 'candidate/fill-user.html', locals())
