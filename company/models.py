from django.db import models
from django.core.urlresolvers import reverse

class Company(models.Model):
    name = models.CharField(max_length=50, null=True)
    eae = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    parent_company = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('company:company_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
