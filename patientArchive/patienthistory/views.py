from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.template import loader
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewPatientForm, PatientVisitForm
from .models import Patient, PatientHistory


#@login_required
def patientHistadd(request, PatientId):
    user = PatientId

    if request.method == "POST":
        form = PatientVisitForm(request.POST, request.FILES)
        if form.is_valid():
            Prescription = form.cleaned_data.get('Prescription')
            nextVisit = form.cleaned_data.get('nextVisit')
            Description = form.cleaned_data.get('Description')
            picture = form.cleaned_data.get('picture')

            p, created = PatientHistory.objects.get_or_create(PatientId=user, Prescription=Prescription,
                                                              nextVisit=nextVisit, Description=Description,
                                                              picture=picture)
            p.save()
            return redirect('home')

    else:
        form = PatientVisitForm()

    context = {
        'form': form,
    }

    return render(request, 'patienthistory/patientVisitForm.html', context)


#@login_required
def patientList(request):
    allProfiles = Patient.objects.all()

    context = {'allProfiles': allProfiles}

    return render(request, 'patienthistory/patientlist.html', context)


##@login_required
def searchPatientByName(request):
    query = request.GET.get("q")
    context = {}

    if query:
        users = Patient.objects.filter(Q(first_name__icontains=query))

        # Pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
        }

    template = loader.get_template('patienthistory/search.html')

    return HttpResponse(template.render(context, request))


#@login_required
def searchPatientById(request):
    query = request.GET.get("q")
    context = {}

    if query:
        users = Patient.objects.filter(Q(Id_card_number__icontains=query))

        # Pagination
        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
        }

    template = loader.get_template('patienthistory/search.html')

    return HttpResponse(template.render(context, request))


#@login_required
def addPatient(request):
    user = request.user.id

    if request.method == "POST":
        form = NewPatientForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone = form.cleaned_data.get('phone')
            about = form.cleaned_data.get('about')
            email = form.cleaned_data.get('email')
            Id_card_number = form.cleaned_data.get('Id_card_number')
            picture = form.cleaned_data.get('picture')
            location = form.cleaned_data.get('location')
            illness = form.cleaned_data.get('illness')

            p, created = Patient.objects.get_or_create( first_name=first_name,
                                                       last_name=last_name, phone=phone, about=about, email=email,
                                                       Id_card_number=Id_card_number, picture=picture,
                                                       location=location, illness=illness)
            p.save()
            return redirect('home')

    else:
        form = NewPatientForm()

    context = {
        'form': form,
    }

    return render(request, 'patienthistory/addPatients.html', context)