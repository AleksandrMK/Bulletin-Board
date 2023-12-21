from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filter import ResponseFilter
from .models import Ad, Response
from .forms import AdForm, ResponseForm, ResponseFormUpdate


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


class AdCreate(LoginRequiredMixin, CreateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_create.html'

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        return super().form_valid(form)


class AdUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'ad_update.html'


class AdDelete(LoginRequiredMixin, DeleteView):
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ads_list')


class ResponseList(LoginRequiredMixin, ListView):
    model = Response
    ordering = 'id'
    template_name = 'response.html'
    context_object_name = 'responses'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponseFilter(self.request.Get, queryset)
        return self.filterset.qs.filter(ad__author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ResponseCreate(LoginRequiredMixin, CreateView):
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'

    def form_valid(self, form):
        response = form.save(commit=False)
        self.ad = get_object_or_404(Ad, id=self.kwargs['ad'])
        response.author = self.request.user
        form.instance.ad = self.ad
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adtitle'] = str(Ad.objects.get(id=self.kwargs['ad']))
        return context


class ResponseDetail(LoginRequiredMixin, DetailView):
    model = Response
    template_name = 'response_detail.html'
    context_object_name = 'response_detail'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("запрос POST")
            response_id = request.POST.get('response_detail_id')
            response = Response.objects.get(id=response_id)
            action = request.POST.get('action')
            if action == 'subscribe':
                response.status = True
                response.save()
            elif action == 'unsubscribe':
                response.status = False
                response.save()
        return render(
            request,
            'response_detail.html',
            {'response_detail': response},
        )


class ResponseUpdate(LoginRequiredMixin, UpdateView):
    form_class = ResponseFormUpdate
    model = Response
    template_name = 'response_update.html'


class ResponseDelete(LoginRequiredMixin, DeleteView):
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('responses')
