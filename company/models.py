from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Company(MPTTModel):
    name = models.CharField(max_length=50, null=True)
    company_estimated_earnings = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='childrens', db_index=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Company.objects.filter(parent=self):
            _r = c.get_all_children(include_self=True)
            if 0 < len(_r):
                r.extend(_r)
        return r

    @property
    def count_earnings(self):
        company_earnings = self.get_all_children()
        total_company_estimated_earnings = 0
        for comp in company_earnings:
            total_company_estimated_earnings += comp.company_estimated_earnings
        return total_company_estimated_earnings
