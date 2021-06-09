from django.shortcuts import render,redirect, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.core.checks.messages import Error
from .models.items import Items
from .models.vendor import Vendor
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password , check_password
from django.views import View

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

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        #validation
        value ={
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone = phone,
                                email= email,
                                password=password)

        error_message = self.validateCustomer(customer)

        
        
        
        print(first_name, last_name, phone, email, password)
        
            
        
        if not error_message:
            

            customer.password = make_password(customer.password)
            customer.register()

            return redirect('storepage')
        else:
            data ={
                'error': error_message,
                'values' : value
            }
            return render(request, 'signup.html', data )

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message= "First name required"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 character long or more"
        elif not customer.last_name:
            error_message="Last name required"
        elif len(customer.last_name) < 4 :
            error_message="last name must be atleast 4 characters"
        elif not customer.phone:
            error_message="Phone number is required"
        elif len(customer.phone) > 10:
            error_message= "phone number should not exceed 10 characters"
        elif len(customer.password) < 6:
            error_message = "Password must be atleast 6 character long"
        elif len(customer.email) < 5:
            error_message = "Email must be atleast 5 character long"
        elif customer.isExists():
            error_message = 'Email Address already registered . . '
            
        return error_message

        
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('storepage')
            else:
                error_message = 'Email or password invalid !!'
        else:
            error_message = 'Email or password invalid !!'

        return render(request, 'login.html', {'error': error_message})

        
        
def logout(request):
    request.session.clear()
    return redirect('login')
    


