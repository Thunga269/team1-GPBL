from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField( max_length=255)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=255)
    phone_number = serializers.CharField( max_length=20)
    email = serializers.EmailField( max_length=255)
    id_company = serializers.CharField(max_length=255)
    class Meta:
        model = Person
        fields = ('id','name', 'age', 'address', 'phone_number', 'email', 'id_company')