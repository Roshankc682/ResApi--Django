from rest_framework import serializers
from emp.models import Exmpmodel
from emp.models import Employeemodel

class serializationclass(serializers.ModelSerializer):
    class Meta:
        model = Exmpmodel
        fields='__all__'

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employeemodel
        fields='__all__'