from .models import Company
from django import forms

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'earnings', 'parent']