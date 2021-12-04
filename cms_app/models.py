from django.db import models
from django.contrib.auth.models import User
from django.utils import tree
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=100,null=True)
    profile_pic=models.ImageField(default='profile1.jpg',null=True,blank=True)
    Date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name or 'name'


class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    desc=models.CharField(max_length=100,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    note=models.CharField(max_length=300,null=True)
    status=models.CharField(max_length=100,null=True,choices=STATUS)
    
    def __str__(self):
        return self.product.name