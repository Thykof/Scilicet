import json


from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


from candidate import forms
from candidate.models import Profile, Category


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                return redirect(reverse('candidate:home'))
            else:
                error = 'Ho zut ! l\'authentification a échoué :/'

                return render(request, "candidate/login.html", locals())

        else:  # invalid form
            error = 'Ho zut ! le formulaire n\'est pas valide :/'
            return render(request, "candidate/login.html", locals())

    else:
        if request.user.is_authenticated:
            return redirect(reverse('candidate:home'))
        else:
            form = forms.LoginForm()
            return render(request, "candidate/login.html", locals())

def signin_view(request):
    error = ''
    if request.method == 'POST':
        form = forms.SigninForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            password_nd = form.cleaned_data["password_nd"]
            email = form.cleaned_data["email"]

            for user in User.objects.all():
                if user.email == email or user.username == last_name:
                    error = 'Ho zut ! cette adresse mail est déjà utilisée (*) :/'
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
                error = 'Ho zut ! les deux mots de passe ne sont pas identiques :/'

        else:  # invalid form
            error = 'Ho zut ! le formulaire n\'est pas valide :/'

    else:  # method = GET
        form = forms.SigninForm()

    return render(request, 'candidate/signin.html', locals())


class ProfileList(ListView):
    model = Profile
    paginate_by = 5
    #template_name = "candidate/profile-list.html"
    #queryset = Profile.objects.all()  # only those with complete name, or at least one item

class ProfileDetail(DetailView):
    model = Profile
    #context_data = User.objects.get(get_full_name=)


def profile_view(request):
    profile = request.user.profile
    items = list()
    for item in profile.items.all():
        items.append((
            item,
            profile.items.filter(category=item.category),
        ))
    return render(request, 'candidate/profile.html', locals())

@login_required
def home_view(request):
    return render(request, 'candidate/home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('candidate:candidate'))

@login_required
def fill_view(request):
    error = ''
    if request.method == 'POST':
        form = forms.ModifyProfile(request.POST)
        if form.is_valid():
            request.user.profile.bio = form.cleaned_data['bio']
            request.user.profile.location = form.cleaned_data['location']
            request.user.profile.birth_date = form.cleaned_data['birth_date']
            request.user.profile.save()
            return redirect(reverse('candidate:home'))
        else:
            error = 'Ho zut ! il y a une erreur dans le formulaire.'
    else:
        form_profile = forms.ModifyProfile(instance=request.user.profile)
        form_item = forms.AddItem(request.user.profile.categories.all())
        form_category = forms.AddCategory()
    return render(request, 'candidate/fill.html', locals())

@login_required
def fill_user_view(request):
    error = ''
    if request.method == 'POST':
        form = forms.ModifyUser(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect(reverse('candidate:home'))
        else:
            error = 'Ho zut ! il y a une erreur dans le formulaire.'
    else:
        form = forms.ModifyUser()
    return render(request, 'candidate/fill-user.html', locals())

@login_required
def add_item(request):
    error = ''
    categories = Category.objects.all()
    if request.method == 'POST':
        form = forms.AddItem(request.user.profile.categories.all(), request.POST)
        if form.is_valid():
            item = form.save()
            request.user.profile.items.add(item)
            return redirect(reverse('candidate:fill'))
        else:
            error = 'Ho zut ! il y a une erreur dans le formulaire.'
    else:
        return redirect(reverse('candidate:fill'))

    return render(request, 'candidate/add-item.html', locals())

@require_http_methods(["POST"])
@login_required
def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        response_data = {}

        category = Category(name=category_name)
        category.save()

        request.user.profile.categories.add(category)

        response_data['result'] = 'Create post successful!'
        response_data['text'] = category.name

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )



def tags_view(request):
    return redirect(reverse('candidate:fill'))
