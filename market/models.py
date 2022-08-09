from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, null=True,blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)  

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False ,null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property 
    def cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.total for item in orderitems])
        
        return total
    
    @property 
    def cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([ item.quantity for item in orderitems])
        
        return total

    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    date_added  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    @property 
    def total(self):
        total_price = self.product.price * self.quantity
        return total_price
    
    
    def __str__(self):
        return self.order

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address