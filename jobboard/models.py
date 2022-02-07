from django.db import models

class Joboffer(models.Model):
    comany_name = models.CharField(max_length=60)
    company_email = models.CharField(max_length=200)
    job_title = models.CharField(max_length=60)
    job_description = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(null=True)

