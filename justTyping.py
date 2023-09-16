import csv

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from djando.views import View
from django.views.generic import premissions, viewsets

from . import models, forms, filters, functions, serializers

# GENERAL WEBSIT NAVIGATION

class Home(View):
    def get(self, request):
        return render(request, 'erp_core/home.html')

class Help(View):
    """Help page"""
    template_name = 'erp_core/help.html'

    def get(self, request):
        return render(request, self.template_name)



class Feature(View):
    """Feature Page"""
    template_name = 'erp_core/feature.html'

    def get(self, request):
        return render(request, self.template_name)



#COMPANY MANAGEMENT

class CompanyCreate(CreateView):
    """Create a new company"""
    model = models.Company
    form_class = forms.CompanyForm
    success_url = reverse_lazy('erp_core:company_list')

class CompanyDetail(DetailView):
    """View a single profile"""
    model = models.Company
    slug_field = 'vat_id'

class companyList(ListView):
    """View all profiles"""
    model = models.Company

    # filter via query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filters.CompanyFilter(self.request.GET, query=self.get_queryset())
        return context

class CompanyUpdate(UpdateView):
    """Update a company"""
    model = models.Company
    form_class = form.CompanyForm
    sucess_url = reverse_lazy('erp_core:company_list')


class CompanyClone(CreateView):
    """Get object desired from url with record.id and override the object context with it."""
    model = models.Company
    form_class.Company
    

