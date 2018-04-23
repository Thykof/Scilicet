from django.urls import path
from django.views.generic import TemplateView


from recruitment import views


app_name = 'recruitment'
urlpatterns = [
    path('', TemplateView.as_view(template_name="recruitment/recruitment.html"), name='recruitment'),
    path('a-propos', TemplateView.as_view(template_name="recruitment/about.html"), name='about'),
    path('accueil', TemplateView.as_view(template_name="recruitment/home.html"), name="home"),
    path('recherche', views.search, name="search"),
]
