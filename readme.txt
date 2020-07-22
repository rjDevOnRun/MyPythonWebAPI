https://www.youtube.com/watch?v=nN2Vp15AW5w

- install python
- install django.. use cmd (pip install django)
- install django Rest Frameworks (pip install djangorestframework)


- in cmd environment
- cd to the location where you want to create the project folder

	Creates an Api project
- < D:\DEVELOPMENT\PYTHON > django-admin startproject MyPythonWebAPI

- cd SampleAPI

	Creates a WebApplication project
- < D:\DEVELOPMENT\PYTHON\MyPythonWebAPI > python manage.py startapp WebAppforAPI


- open folder in VSCode
	- add required codes to 

----------------------------------------------------------------------
	  settings.py (register frmwork and our web-app)
	
#1: under the 'INSTALLED_APPS' section		
	Add below line....
		'rest_framework',
		'WebAppforAPI'


----------------------------------------------------------------------
	  views.py (add action method)
	
#1: add imports...

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

#2: under the views...		
	@api_view(['POST'])
	def IdealWeight(heightdata):
	    try:
        	height=json.loads(heightdata.body)
	        weight=str(height * 10)

	        return JsonResponse("Ideal weigh: " + weight + " kg", safe=False)
    
	    except ValueError as e:
	        return Response(e.args[0], status.HTTP_404_NOT_FOUND)

----------------------------------------------------------------------
	  urls.py (for routing to appropriate actions)

#1: add imports...
	from django.conf.urls import url
	from django.contrib import admin
	from WebAppforAPI import views <<<------



#1: under the "'urlpatterns'" section		
	add below code:
	
	url(r'^admin/', admin.site.urls),
	url(r'^idealweight/', views.IdealWeight)

----------------------------------------------------------------------

- Save all

- in cmd environment

	Runs the webapi server
- < D:\DEVELOPMENT\PYTHON\SampleAPI > python manage.py startapp MyWebApp

- Open 'POSTMAN'
- Request a Http 'POST' to url
- in body send the parameter value