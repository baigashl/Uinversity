from django.contrib import messages
from django.shortcuts import render, redirect

from apps.accounts.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Wellcome {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return redirect(request, 'accounts/register.html', {'form': form})

def login(request):
    return render(request, 'accounts/login.html')

def index(request):
    return render(request, 'index.html')


# Create your views here.
