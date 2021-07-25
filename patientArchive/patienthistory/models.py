from django.db import models
import uuid
from django.contrib.auth.models import User


class Patient(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    drId = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True, null=True, verbose_name='Picture')
    phone = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    Id_card_number = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    illness = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} for dr.{self.drId.username} / id: {self.Id_card_number}'

    # def get_absolute_url(self):
    #     return reverse('postdetails', args=[str(self.id)])


class PatientHistory(models.Model):
    PatientId = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    Prescription = models.TextField(max_length=300, null=True, blank=True)
    nextVisit = models.DateTimeField(null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True, null=True, verbose_name='Picture')
    VisitDate = models.DateTimeField(auto_now_add=True, blank=True)
    Description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'Patient {self.PatientId.first_name}\'s visit on {self.VisitDate}'

# %Y-%m-%d %H:%M:%S