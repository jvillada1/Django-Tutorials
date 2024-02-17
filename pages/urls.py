from django.urls import path,include
from .views import HomePageView, AboutPageView,ContactPageView, ProductIndexView,ProductShowView,ProductCreateView
from django.contrib import admin 


urlpatterns = [
    #path('home/', HomePageView.as_view(), name='home'),  
    path("", HomePageView.as_view(template_name="home.html"), name="home"), 
    path('about/', AboutPageView.as_view(), name='about'), 
    path('contact/', ContactPageView.as_view(), name='contact'), 
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'), 

    path('products/<str:id>', ProductShowView.as_view(), name='show'), 



]
