from django.shortcuts import render
from .models import Profile, Patient, Doctor, Appointment
from .serializers import profileserializer, patientserializer, doctorserializer, appointmentserializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView, \
    UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import OrderingFilter
from rest_framework.throttling import UserRateThrottle
from django.http import HttpResponse


# Create your views here.

class CreateProfile(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = profileserializer


class CreatePatient(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Patient.objects.all()
    serializer_class = patientserializer

    def perform_create(self, serializer):
        return serializer.save(user_name=self.request.user)

    def get_queryset(self):
        return Patient.objects.filter(user_name=self.request.user)


class CreateDoctor(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = doctorserializer


class CreateAppointment(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = appointmentserializer


class AddFilterView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = profileserializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['user_name', 'user_id', 'password']


class ProfileList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = profileserializer


class PatientList(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = patientserializer

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('user_name', None)
        if author is not None:
            queryset = queryset.filter(author__name=author)
        return queryset


class AppointmentList(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = appointmentserializer


class UpdatePatient(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    throttle_classes = [UserRateThrottle]

    queryset = Patient.objects.all()
    serializer_class = patientserializer

    def perform_update(self, serializer, partial=False):
        # Update the object using the serializer
        serializer.save(partial=partial)


class DeletePatient(DestroyAPIView):
    queryset = Patient.objects.all()


class Deleteprofile(DestroyAPIView):
    queryset = Profile.objects.all()


class retrieveupdateview(RetrieveUpdateAPIView):
    queryset = Profile.objects.all
    serializer_class = profileserializer


class retieveupdatepatient(RetrieveUpdateAPIView):
    queryset = Patient.objects.all
    serializer_class = patientserializer



class RetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = appointmentserializer


