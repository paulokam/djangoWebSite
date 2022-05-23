from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class ProPageView(TemplateView):
    template_name = "pro.html"

class PersonalPageView(TemplateView):
    template_name = "personal.html"