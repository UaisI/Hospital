from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return f'Dr.{self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=22, choices=GENDER_CHOICES)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=22, decimal_places=2)

    def __str__(self):
        return self.name
class Visit(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    date_and_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.doctor.first_name}{self.doctor.last_name}-{self.patient.full_name}-{self.date_and_time} '
