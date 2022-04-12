from django.views.generic import TemplateView


class PopularTripView(TemplateView):
    template_name = 'main/home_page.html'

