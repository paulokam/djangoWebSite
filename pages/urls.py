from django.urls import path

from .views import HomePageView, ProPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('minha-historia-profissional/', ProPageView.as_view(), name='pro'),
    

]