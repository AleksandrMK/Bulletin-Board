from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Ad


class AdsList(ListView):
    model = Ad
    ordering = 'date_create'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 2


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
