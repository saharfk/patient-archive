from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return render(request, 'patienthistory/home.html')
    else:
        return render(request, 'patienthistory/login.html')

