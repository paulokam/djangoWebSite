from django.urls import path
from traitlets import import_item

from .views import HomePageView, ProPageView, PersonalPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('minha-historia-profissional/', ProPageView.as_view(), name='pro'),
    path('minha-historia-pessoal/', PersonalPageView.as_view(), name='personal'),
]