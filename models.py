from django.db import models

# Create your models here.

gender = (('Male', 'Male'),
          ('Female', 'Female'),
          ('others', 'others'))

reasons = (
    ("IPD", "In-patient"),
    ("OPD", "Out-patient"),
    ("sugar-test", "sugar-test"),
    ("body-checkup", "Body-checkup"),
    ("IOT", "Health Analysis"),
)

category = (
    ("Dermatology", "Dermatologist"),
    ("neurology", "Neurologist"),
    ("surgeon", "surgeon"),
    ("cardiology", "cardiologist"),
    ("General_surgery", "General_surgery"),
)


class Profile(models.Model):
    user_name = models.CharField(max_length=50, null=False)
    user_id = models.IntegerField()
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.user_name


class Patient(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=20, choices=gender, default='Male')
    age = models.IntegerField(null=False)
    Reason_for_visit = models.CharField(max_length=100, choices=reasons, default='body-checkup')
    phone_num = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.user_name


class Doctor(models.Model):
    name = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
    specialization = models.CharField(max_length=100, choices=category, default='surgeon')
    license_number = models.CharField(max_length=50, null=False)
    phone_no = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.specialization


class Appointment(models.Model):
    appointment_id = models.CharField(max_length=50, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False)
    booking_date = models.CharField(max_length=50, null=False)
    booking_time = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.appointment_id


