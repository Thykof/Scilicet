from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


from candidate import views


app_name = 'candidate'
urlpatterns = [
    path('connexion', views.login_view, name='login'),
    path('inscription', views.signin_view, name='signin'),
    path('', views.home_view, name='home'),
    path('candidat', TemplateView.as_view(template_name="candidate/candidate.html"), name='candidate'),
    path('info', TemplateView.as_view(template_name="candidate/howto.html"), name='howto'),
    path('deconnexion', views.logout_view, name='logout'),
    path('remplir', views.fill_view, name='fill'),
    path('remplir-identite', views.fill_user_view, name='fill-user'),
    path('ajouter-section', views.add_item, name='add-item'),
    path('ajouter-categorie', views.add_category, name='add-category'),

    #url('accounts/', include('django.contrib.auth.urls')),
    # This include:
    #accounts/login/ [name='login']
    #accounts/logout/ [name='logout']
    #accounts/password_change/ [name='password_change']
    #accounts/password_change/done/ [name='password_change_done']
    #accounts/password_reset/ [name='password_reset']
    #accounts/password_reset/done/ [name='password_reset_done']
    #accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    #accounts/reset/done/ [name='password_reset_complete']

    # Specific generic view:
    #url(
    #    'change-password',
    #    auth_views.password_change,
    #    {'template_name': 'change-password.html'}
    #),
]
