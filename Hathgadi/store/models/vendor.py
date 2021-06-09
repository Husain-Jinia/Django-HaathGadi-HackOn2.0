from django.db import models
from .items import Items

# Create your models here.

class Vendor(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "upload/vendors/", null=True, blank=True)
    adhar_no = models.CharField(max_length=10)
    items = models.ManyToManyField(Items, related_name="vendors")


    def __str__(self):
        return f"{self.first} {self.last}"