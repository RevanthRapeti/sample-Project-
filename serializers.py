from rest_framework import serializers
from .models import Profile, Patient, Doctor, Appointment


class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class patientserializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class doctorserializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class appointmentserializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
