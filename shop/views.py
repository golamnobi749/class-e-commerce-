from django.shortcuts import render
from django.views import View
from  .models import Customer,Product,Cart,OrderPlaces


# Create your views here.
def home(request):
    return render(request, 'shoping/base.html')
class TshirtView(View):
   def get(self,request):
        tshirt = Product.objects.filter(category='T shirt')
        lehenga= Product.objects.filter(category='lehenga')
        burkha = Product.objects.filter(category='burkha')
        return render(request,'shoping/tshirt.html',{'tshirt':tshirt,'lehenga':lehenga,'burkha':burkha})
    
class ProductViews(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'shoping/tshirtview.html',{'tview':product})

        
