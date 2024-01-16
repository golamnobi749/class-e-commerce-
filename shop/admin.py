from django.contrib import admin
from  .models import Customer,Product,Cart,OrderPlaces

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','name','division','district','upazila','contact','village_road','zipcode')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('subcategory', 'productname', 'description','price','current_price','brand','quantity','category','image','status','created_at','updated_at')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','product','total_amount','quantity')
@admin.register(OrderPlaces)
class OrderPlaceAdmin(admin.ModelAdmin):
    list_display = ('user','product','customer','quantity','order_date','city','state')