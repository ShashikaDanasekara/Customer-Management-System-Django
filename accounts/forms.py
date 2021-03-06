from pyexpat import model
from attr import field
from django.forms import ModelForm
from .models import Customer, Order, Product

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class OrderFrom(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ProductFrom(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CustomerFrom(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']









