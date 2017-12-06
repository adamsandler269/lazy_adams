from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"))
]
