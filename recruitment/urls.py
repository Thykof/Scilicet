from django.urls import path
from django.views.generic import TemplateView


from recruitment import views
from candidate import views as candidate_views


app_name = 'recruitment'
urlpatterns = [
    path('', TemplateView.as_view(template_name="recruitment/recruitment.html"), name='recruitment'),
    path('a-propos', TemplateView.as_view(template_name="recruitment/about.html"), name='about'),
    path('recherche', candidate_views.ProfileList.as_view(), name="search"),
]
