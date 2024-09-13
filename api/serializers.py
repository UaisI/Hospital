from rest_framework import serializers

from .models import Doctor, Service, Visit


# class DoctorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = '__all__'

class DoctorListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    contact_info = serializers.CharField()



class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'contact_info']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DoctorPatientsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()



class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


