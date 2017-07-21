from django.views import generic
from company.models import Company
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'company/index.html'
    context_object_name = 'company_list'

    def get_queryset(self):
        return Company.objects.all()

class AddView(generic.CreateView):
    template_name = 'company/add.html'
    model = Company
    fields = ['name', 'eae', 'parent_company']
    success_url = reverse_lazy('company:index')

class DetailView(generic.DetailView):
    model = Company
    template_name = 'company/detail.html'

class CompanyEdit(generic.UpdateView):
    model = Company
    fields = ['name', 'eae', 'parent_company']
    success_url = reverse_lazy('company:index')

class CompanyDelete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy('company:index')
