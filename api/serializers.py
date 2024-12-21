from rest_framework import serializers
from api.models import Company,Employee
#create a serializer for the model

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    compaany_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class EmpoyeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"