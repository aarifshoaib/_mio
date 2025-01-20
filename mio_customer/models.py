from django.db import models
class tbl_customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)
    customer_type = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    tags = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    visibility = models.CharField(max_length=10)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name