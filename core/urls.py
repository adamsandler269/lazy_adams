from django.urls import path
from django.views.generic import TemplateView
app_name = 'core'
# Create your views here.
urlpatterns = [
    path('', TemplateView.as_view(template_name="core/home.html"), name='home')
]
