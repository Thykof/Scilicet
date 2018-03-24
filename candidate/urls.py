from django.urls import path


from candidate import views


urlpatterns = [
    path('connexion', views.login, name='login'),
    path('inscription', views.signin, name='signin'),
]
