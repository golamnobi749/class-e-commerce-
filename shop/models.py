from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DIVISION_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('sylhet', 'sylhet'),
    ('mymenshing','mymenshing'),
    ('chittagong','chittagong'),
    ('Barishal', 'Barishal'),
    ('khulna','khulna'),
    ('rangpur','rangpur'),
    ('rajshahi','rajshahi')
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    division = models.CharField(choices = DIVISION_CHOICES, max_length=200)
    district = models.CharField(max_length=150,blank=True)
    upazila = models.CharField(max_length=150,blank=True)
    contact = models.IntegerField()
    village_road = models.CharField(max_length=150,blank=True)
    zipcode = models.IntegerField()
    def __str__(self):
        return str(self.id)
CATEGORY_CHOICES = (
    ('T shirt','T shirt'),
    ("Jeans","Jeans"),
    ("Shirt", "Shirt"),
    ("BABY DRESS", "BABY DRESS"),
    ("Kurta Salwar", "Kurta Salwar"),
    ('burkha','Burkha'),
    ('lehenga','Lehenga'),
)
class Product(models.Model):
    subcategory = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField()
    current_price = models.FloatField()
    brand = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length=12)
    image = models.ImageField(upload_to='product/images/', null=True)
    status = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=9,decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)
def __str__(self):
    return str(self.id)
PENDING_CHOICES = (
        ('pending','Pending'),
        ('processing','Processing'),
        ('delivered','Delivered'),
        ('deleted','deleted'),
        ('accepted','accepted'),
        ('On The way','On the way'),
                   )
class OrderPlaces(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)
    order_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices =PENDING_CHOICES,default='pending')

