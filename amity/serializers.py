from .models import Student
from rest_framework import serializers
from amity.models import Block

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    enrollment = serializers.CharField(max_length=40)
    phone = serializers.CharField(max_length=15)
    email = serializers.EmailField()


    def create(self, validated_data):
        print("create method called ")
        return Student.objects.create(**validated_data)

    def update(self, student, validated_data):
        newStudent = Student(**validated_data)
        newStudent.id = student.id;
        newStudent.save()
        return newStudent




class BlockSerializer(serializers.Serializer):
    dish_name = serializers.CharField(max_length=40)
    price = serializers.CharField(max_length=40)
    image = serializers.CharField(max_length=15)


    def create(self, validated_data):
        print("create method called ")
        return Block.objects.create(**validated_data)

    def update(self, Block, validated_data):
        newBlock = Block(**validated_data)
        newBlock.id = Block.id;
        newBlock.save()
        return newBlock

