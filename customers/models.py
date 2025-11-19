from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

class Client(TenantMixin):
    name = models.CharField(max_length=255)
    paid_until = models.DateField(null=True)
    on_trial = models.BooleanField(default=True)
    # required
    auto_create_schema = True

class Domain(DomainMixin):
    pass
