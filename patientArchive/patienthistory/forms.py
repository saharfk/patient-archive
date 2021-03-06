from django import forms
from .models import Patient


class dateInput(forms.DateInput):
    input_type = 'date'


class NewPatientForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), max_length=50,
                                 required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), max_length=50,
                                required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), max_length=300,
                            required=True)
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), max_length=30,
                            required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input is-medium'}), max_length=100,
                             required=False)
    Id_card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}),
                                     required=True)
    picture = forms.ImageField(required=False)

    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), max_length=25,
                               required=False)
    illness = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), max_length=25,
                              required=False)

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'phone', 'email', 'Id_card_number', 'picture', 'location', 'illness')


class PatientVisitForm(forms.ModelForm):
    Prescription = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), max_length=300,
                                   required=True)
    nextVisit = forms.CharField(required=False, widget=dateInput, max_length=30)
    Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), max_length=300,
                                  required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = Patient
        fields = ('Prescription', 'nextVisit', 'Description', 'picture')
