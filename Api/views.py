
from django.shortcuts import render

# Create your views here.
from .models import Student,Card
from rest_framework import viewsets
#from rest_framework import permissions
from .serializers import StudentSerializer,CardSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('course')
    serializer_class = StudentSerializer
    #permission_classes = [permissions.IsAuthenticated]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('cardno')
    serializer_class = CardSerializer    

