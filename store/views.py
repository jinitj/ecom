from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Accounted created for {username}')
            return redirect('store-home')

    else:
        form=UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})


def index(request):
    return render(request, 'store/home.html')