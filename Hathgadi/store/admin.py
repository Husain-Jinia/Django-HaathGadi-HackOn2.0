from django.contrib import admin
from .models.items import Items
from .models.vendor import Vendor
from .models.category import Category
from .models.customer import Customer

# Register your models here.

admin.site.register(Items)
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Customer)
