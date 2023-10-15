from django.views import View
from django.shortcuts import render
from .forms import UserRegisterForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect


class RegisterView(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return HttpResponseRedirect(reverse('login'))
        return render(request, 'users/register.html', {'form': form})



