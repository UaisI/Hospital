from django.shortcuts import render
from rest_framework import generics, viewsets, mixins

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.mixin import HospitalGenericViewSet
from api.models import Patient

from api.my_serializers.patient import PatientsSerializer, PatientDetailSerializer, PatientUpdateorCreateSerializer


class PatientView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender']
    search_fields = ['first_name', 'last_name']

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_patient', ]
        elif self.action == 'create':
            self.action_permissions = ['add_patient']
        elif self.action == 'update':
            self.action_permissions = ['change_patient']
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient']

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientsSerializer
        if self.action == 'retrieve':
            return PatientDetailSerializer
        if self.action == 'create':
            return PatientUpdateorCreateSerializer
        if self.action == 'update':
            return PatientUpdateorCreateSerializer

    def get_queryset(self):  # Этот метод уже существует в DRF в GenericViewSet, дальше мы его переопределяем
        return Patient.objects.all()
