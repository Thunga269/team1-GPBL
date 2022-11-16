from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib
from urllib import parse
from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class ListPersonView(APIView):
    def get(self, request, format=None):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request):
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
# put and delete person
class UpdatePersonView(APIView):  
    def get(self, request, id):
        # ids  = request.GET.get('id')
        # name = parse.unquote(name)
        PersonById = Person.objects.filter(id=id)
        serializer = PersonSerializer(PersonById, many=True)
        return Response(serializer.data)
    def delete(self, request,id ,*args, **kwargs):
        # name  = request.GET.get('id')
        # name = parse.unquote(name)
        print(id)
        person = Person.objects.filter(id=id)
        person.delete()
        return JsonResponse({
                'message': 'Delete a new person successfully'
            }, status = status.HTTP_204_NO_CONTENT)    
        
    def put(self, request, id):
        # name = request.GET.get('id')
        # name = parse.unquote(name)
        person = Person.objects.get(id=id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update a new person successfully'
            }, status = status.HTTP_201_CREATED)
        else:
            return JsonResponse({
                'message': 'Update unsuccessfully'
            }, status = status.HTTP_400_BAD_REQUEST)     