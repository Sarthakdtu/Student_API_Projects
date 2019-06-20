#from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
#from django.http import Http404
#from rest_framework.views import APIView
from rest_framework import mixins, generics, permissions
from .models import Student
from django.contrib.auth.models import User
from .serializers import StudentSerializer, SchoolSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

#Students
class student_list(generics.ListCreateAPIView):
    print(User)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes =(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(school=self.request.user)

class student_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes =(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

#School
class SchoolList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = SchoolSerializer

class SchoolDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SchoolSerializer


class SchoolStudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self, *args, **kwargs):
        return Student.objects.filter(school=self.kwargs['pk'])


class SchoolStudentDetails(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self, *args, **kwargs):
        return Student.objects.filter(pk=self.kwargs['student_pk'], school=self.kwargs['school_pk'])






#Class Based Views using mixins

"""
class student_list( mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    print("Here")
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class student_details( mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



"""




"""
#A simple serialization view

@csrf_exempt
def student_list(request):

    #List all code students, or create a new student.


    print("At list", request)
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        print(serializer)
        print("Data ", serializer.data)
        response = JsonResponse(serializer.data, safe =False)
        print(response)
        return response
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 404)


@csrf_exempt
def student_details(request, pk):
    print(request)
    try:
        student = Student.objects.get(pk=pk)
        print("yep")
    except Student.DoesNotExist:
        print("Nope")
        return HttpResponse(status=404)

    if request.method=='GET':
        print("At get")
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        print("At del")
        student.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        print("At put")
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
"""




#Function Based Views

"""
@api_view(['GET', 'POST'])
def student_list(request):
    #List all code students, or create a new student.
    print("At list", request)
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        print(serializer)
        print("Data ", serializer.data)
        response = Response(serializer.data)
        print(response)
        return response
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):
    print(request)
    try:
        student = Student.objects.get(pk=pk)
        print("yep")
    except Student.DoesNotExist:
        print("Nope")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        print("At get")
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        print("At del")
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        print("At put")
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
