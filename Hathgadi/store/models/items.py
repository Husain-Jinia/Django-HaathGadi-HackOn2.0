from django.db import models
from .category import Category

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length = 50)
    description = models.CharField(max_length=50, default='')
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="upload/items/", default='')


    def __str__(self):
        return self.name


    @staticmethod
    def get_all_items():
        return Items.objects.all()

    @staticmethod
    def get_all_items_by_category_id(category_id):
        if category_id:
            return Items.objects.filter(category = category_id)
        else:
            return Items.get_all_items()
