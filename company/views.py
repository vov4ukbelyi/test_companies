from django.views import generic
from .forms import CompanyForm
from django.db.models import Sum
from company.models import Company
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'company/index.html'
    context_object_name = 'company_list'


    def get_queryset(self):
        return Company.objects.all()


class AddView(generic.CreateView):
    template_name = 'company/add.html'
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company:index')

class DetailView(generic.DetailView):
    model = Company
    template_name = 'company/detail.html'

class CompanyEdit(generic.UpdateView):
    model = Company
    success_url = reverse_lazy('company:index')
    form_class = CompanyForm


class CompanyDelete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy('company:index')

'''class TreeView(generic.ListView):
    template_name = 'company/tree.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        return Company.objects.annotate(total_eae=Sum('eae'))
'''

def show_companies(request):
    return render(request, 'company/tree.html', {'nodes':Company.objects.all()})