from django.contrib import admin
from .models import Specialization, Patient, Visit, Service, Doctor


admin.site.register(Specialization)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Service)
admin.site.register(Doctor)
# Register your models here.
