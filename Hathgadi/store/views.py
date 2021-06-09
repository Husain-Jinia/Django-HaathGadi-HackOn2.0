from django.shortcuts import render
from .models.items import Items
from .models.vendor import Vendor
from .models.category import Category

# Create your views here.

def store(request):
    items = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        items = Items.get_all_items_by_category_id(categoryID)
    else:
        items = Items.get_all_items()
    data = {}
    data['items'] = items
    data['categories'] = categories

    return render(request, 'store.html',data)

def Vendors(request, items_id):
    items = Items.objects.get(id = items_id)
    return render(request, 'vendor.html',{'items':items,'vendors': items.vendors.all() })




