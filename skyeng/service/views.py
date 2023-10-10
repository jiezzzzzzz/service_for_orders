from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required


@login_required()
def orders(request):
    orders = Product.objects.all()
    context = {'orders': orders}
    return render(request, 'service/index.html', context)

