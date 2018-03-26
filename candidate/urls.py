from django.urls import path


from candidate import views


app_name = 'candidate'
urlpatterns = [
    path('connexion', views.login, name='login'),
    path('inscription', views.signin, name='signin'),
]
