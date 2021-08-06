from django.shortcuts import render, redirect
from  emp.serialization import serializers
from  emp.serialization import serializationclass
from emp.models import Exmpmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from  emp.serialization import Employeemodel
from  emp.serialization import Employeeserializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def showemp(reques):
    if reques.method == 'GET':
        result=Exmpmodel.objects.all()
        serializer=serializationclass(result,many=True)
        return Response(serializer.data)

def displatdata(request):
    callapi = requests.get('http://127.0.0.1:8000/show')
    results = callapi.json()
    print(callapi)
    print(results)
    return render(request,'show.html',{'Emp':results})


@api_view(['POST'])
def saveemp(request):
    if request.method == "POST":
        saveserialize = Employeeserializer(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            print(request.data)
            # return redirect('/saveemp')
            print("Hit")
            return Response(saveserialize.data,status=status.HTTP_201_CREATED)
        print("hit hited")
        return Response(saveserialize.data.status,status=status.HTTP_400_BAD_REQUEST)
        # return redirect('/saveemp')

def insertemp(request):
    if request.method == "POST":
        empname = request.POST.get('empname')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        data = {"empname":empname,"email":email,"salary":salary}
        print(data)
        headers={"Content-Type": 'application/json'}
        print(headers)
        read = requests.post('http://127.0.0.1:8000/saveemp',json=data,headers=headers)
        print(read)
        return render(request,'insert.html')
    else:
        return render(request,'insert.html')




























