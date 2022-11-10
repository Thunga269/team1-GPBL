from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class ListPersonView(APIView):
    def get(self, request, format=None):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new person successfully'
            }, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse({
                'message': 'Create a new person unsuccessfully'
            }, status = status.HTTP_400_BAD_REQUEST)