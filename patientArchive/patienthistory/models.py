from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.drId.id, filename)


def user_hitory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'hist{0}/{1}'.format(instance.PatientId.id, filename)

class Patient(models.Model):
    drId = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Picture')
    phone = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    Id_card_number = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    illness = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} for dr.{self.drId.username} / id: {self.Id_card_number}'


class PatientHistory(models.Model):
    PatientId = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    Prescription = models.TextField(max_length=300, null=True, blank=True)
    nextVisit = models.CharField(null=True, blank=True, max_length=30)
    picture = models.ImageField(upload_to=user_hitory_path, blank=True, null=True, verbose_name='Picture')
    VisitDate = models.DateTimeField(auto_now_add=True, blank=True)
    Description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'Patient {self.PatientId.first_name}\'s visit on {self.VisitDate}'
