
from .models import Student,Card
from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student 
        fields = ('student_name', 'gender', 'course', 'session','date_of_birth','address','religion','telephone_no','nationality','marital_status')

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card 
        fields = ('student', 'cardno', 'barcode', 'status')

