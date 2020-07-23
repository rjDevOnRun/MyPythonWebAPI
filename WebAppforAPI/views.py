from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.

@api_view(['POST'])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height * 10)

        return JsonResponse("Ideal weigh: " + weight + " kg", safe=False)
    
    except ValueError as e:
        return Response(e.args[0], status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def GetSquaresOf(numberdata):
    try:
        nums=json.loads(numberdata.body)
        squaredNums=str()
        sqrNum = ""

        for n in nums:
            if isinstance(n, int):
                sqrNum = str(n * n)
            elif isinstance(n , float):
                sqrNum = str(float(n) * float(n))
            elif n.isdigit():
                sqrNum = str(int(n) * int(n))
            elif n.replace('.', '', 1).isdigit() and n.count('.') < 2:
                sqrNum = str(float(n) * float(n))
            else:
                sqrNum = str(int(n) * int(n))
        
            if len(squaredNums) < 1:
                squaredNums = sqrNum
            else:
                squaredNums += ", " + str(sqrNum)

        return JsonResponse("Squared Numbers: " + squaredNums, safe=False)
    
    except ValueError as e:
        return Response(e.args[0], status.HTTP_404_NOT_FOUND)
