
from django.db import models
from provider.models import ProviderList

class CustomerList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    code = models.CharField(max_length=20)
    provider = models.ForeignKey(ProviderList, on_delete=models.CASCADE, related_name='customers')

    def __str__(self):
        return self.name
