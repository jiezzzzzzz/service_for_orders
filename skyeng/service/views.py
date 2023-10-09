from django.shortcuts import render
from .models import Product

def orders(request):
    orders = Product.objects.all()
    context = {'orders': orders}
    return render(request, 'service/index.html', context)
