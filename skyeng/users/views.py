from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'users/register.html', {'form': form})



