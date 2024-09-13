from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import DoctorFilterSet
from .mixin import HospitalGenericViewSet
from .models import Doctor, Service, Visit, Patient
from .serializers import DoctorListSerializer, DoctorCreateSerializer, DoctorRetrieveSerializer, DoctorUpdateSerializer
from .serializers import ServiceSerializer, VisitSerializer, DoctorPatientsListSerializer
from .permissions import DoctorAccessPermissions, RoleBasedPermissionsMixin, HasPermissionsByAuthenticatedUserRole
from django_filters.rest_framework import DjangoFilterBackend

# class DoctorListCreateView(generics.ListCreateAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer


class DoctorView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'specialization']

    filterset_class = DoctorFilterSet

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient']
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return DoctorPatientsListSerializer

    def get_queryset(self): #Этот метод уже существует в DRF в GenericViewSet, дальше мы его переопределяем
        if self.action == 'list_patient':
            return Patient.objects.all()
        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits__doctor_id=id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)


class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.all()


class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin

):
    serializer_class = VisitSerializer

    def get_queryset(self):
        return Visit.objects.all()
