from django.urls import path
from Reception.views import CreateProfile, CreatePatient, AddFilterView, PatientList,\
    UpdatePatient, DeletePatient, retrieveupdateview, ProfileList, retieveupdatepatient, \
    CreateDoctor, CreateAppointment, AppointmentList, Deleteprofile, RetrieveDestroyView

urlpatterns =[
    path('profile', CreateProfile.as_view(), name='CreateProfile'),
    path('profile-list', ProfileList.as_view(), name='ProfileList'),
    path('create-patient', CreatePatient.as_view(), name='CreatePatient'),
    path('create-doctor', CreateDoctor.as_view(), name='CreateDoctor'),
    path('create-appointment', CreateAppointment.as_view(), name='CreateAppointment'),
    path('filter_list', AddFilterView.as_view(), name='AddFilterView'),
    path('patient-list', PatientList.as_view(), name='PatientList'),
    path('appointment-list', AppointmentList.as_view(), name='AppointmentList'),
    path('update-patient/<int:pk>/', UpdatePatient.as_view(), name='UpdatePatient'),
    path('delete-profile/<int:pk>/', Deleteprofile.as_view(),name='Deleteprofile'),
    path('delete-patient/<int:pk>/', DeletePatient.as_view(), name='DeletePatient'),
    path('retrieveupdate-profile/<int:pk>/', retrieveupdateview.as_view(), name='retrieveupdateview'),
    path('retieveupdate-patient/<int:pk>/', retieveupdatepatient.as_view(), name="retieveupdatepatient"),
    path('Edit-appoinments/<int:pk>/', RetrieveDestroyView.as_view(), name='RetrieveDestroyView'),

]