from django.urls import path
from .views import EventListView

app_name = "events"
urlpatterns = [
    path('minha-historia-pessoal/', EventListView.as_view(), name='personal'),
]