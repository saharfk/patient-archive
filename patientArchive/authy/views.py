from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
    # , EditProfileForm
# from .models import Profile
from django.contrib.auth.models import User

# Create your views here.

# def Signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('sername')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('home')
#
#     else:
#         form = SignupForm()
#     return render(request, 'patienthistory/signup.html', {'form': form})


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

#
# def EditProfile(request):
#     user = request.user.id
#     profile = Profile.objects.get(user__id=user)
#
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile.picture = form.cleaned_data.get('picture')
#             profile.first_name = form.cleaned_data.get('first_name')
#             profile.last_name = form.cleaned_data.get('last_name')
#             profile.location = form.cleaned_data.get('location')
#             profile.url = form.cleaned_data.get('url')
#             profile.profile_info = form.cleaned_data.get('profile_info')
#             profile.save()
#             return redirect('index')
#     else:
#         form = EditProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'edit_profile.html', context)
