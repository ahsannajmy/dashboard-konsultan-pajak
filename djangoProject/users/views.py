from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('user_role')
            messages.success(request, f'Akun {role} berhasil dibuat untuk {username}')
            return redirect('dashboard-home')
    else:
        form = CustomUserCreationForm()

    return render(request,'users/register.html', {'form': form})