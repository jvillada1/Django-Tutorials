##from django.shortcuts import render # here by default
##from django.http import HttpResponse # new
from django.views.generic import TemplateView 
from django.views import View 
from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse 
from django import forms
from django.shortcuts import render, redirect


# Create your views here.
##def homePageView(request): # new
	##return HttpResponse('Hello World!') # new
class HomePageView(TemplateView): 
    template_name = 'home.html' 
    

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })

        return context 
    

class ContactPageView(TemplateView): 
    template_name = 'pages/about.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact",
            "subtitle": "Contact us",
            "description": "cell: 30939453490  djangoproject@django.com", 

        })

        return context 



class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV","price":"50"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone","price":"6000"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast","price":"4000"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses","price":"20"}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id) - 1]
        except IndexError:
            # Product number is not valid, redirect to home page
            return HttpResponseRedirect(reverse('home'))

        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData) 


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True) 
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price


class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Save the product or perform any necessary actions
            # For demonstration, we're just redirecting to a success page
            return render(request, 'products/product_created.html')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)