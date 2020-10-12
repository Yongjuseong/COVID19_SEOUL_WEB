from django.views.generic import ListView, DetailView
from agency.models import Agency


class AgencyLV(ListView):
    model = Agency

class AgencyDV(DetailView):
    model = Agency

