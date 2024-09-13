from rest_framework import serializers

from api.models import Patient


class PatientsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    birth_date = serializers.DateField()
    gender = serializers.CharField()


class PatientDetailSerializer(PatientsSerializer):
    contact_info = serializers.CharField()


class PatientUpdateorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
