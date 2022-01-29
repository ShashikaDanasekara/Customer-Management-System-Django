from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(default="default-avatar.png",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} {1}'.format(self.id, self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORIES = (
        ('Indoors','Indoors'),
        ('Outdoor','Outdoor'),
        ('Sports','Sports'),
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(max_length=200,null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORIES)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Processing','Processing'),
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for delivary','Out for delivary'),
    )
    customer = models.ForeignKey(Customer,blank=True, null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,blank=True, null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=200,null=True,choices=STATUS,default='Processing')
    date_created = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.product.name
