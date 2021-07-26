from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.models import User


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'patienthistory/signup.html', context)


