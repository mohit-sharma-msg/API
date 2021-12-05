from .models import Student
from .serializers import StudentSerializer
from .models import Block
from .serializers import BlockSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def studentListView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = StudentSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET', 'POST'])
def blockListView(request):
    if request.method == 'GET':
        block = Block.objects.all()
        serializer = BlockSerializer(block, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = BlockSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



    if request.method == "PUT":
        serializer = BlockSerializer(block, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)




