from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class RegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','email','password1','password2']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields='__all__'

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"

class UserOrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['customer',]

class CreateCustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"