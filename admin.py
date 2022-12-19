from django.contrib import admin
from .models import Profile, Patient, Doctor, Appointment


# Register your models here.
class profileadmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_id', 'password')


class patientadmin(admin.ModelAdmin):
    list_display = ('user_name', 'gender', 'age', 'Reason_for_visit', 'phone_num')


class doctoradmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'license_number', 'phone_no')


class appointmentadmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'patient', 'doctor', 'booking_date', 'booking_time')


admin.site.register(Profile, profileadmin)
admin.site.register(Patient, patientadmin)
admin.site.register(Doctor, doctoradmin)
admin.site.register(Appointment, appointmentadmin)


