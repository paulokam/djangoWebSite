from django.urls import path
from .views import EventListView

app_name = "events"
urlpatterns = [
    path('minha-historia-profissional/', EventListView.as_view(), name='pro'),
]