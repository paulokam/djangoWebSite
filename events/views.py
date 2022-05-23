from django.views.generic import TemplateView


class EventDetailView(TemplateView):
    template_name = "event.html"
