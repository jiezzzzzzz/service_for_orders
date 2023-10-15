from django.views import View
from django.shortcuts import render
from .models import Order


class OrdersView(View):
    def get(self, request):
        orders = Order.objects.all()
        context = {'orders': orders}
        if request.user.is_authenticated:
            return render(request, 'service/index.html', context)

