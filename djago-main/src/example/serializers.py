from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'age', 'address', 'phone_number', 'email', 'id_company')