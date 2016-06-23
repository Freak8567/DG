from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory


from api.models import Data
from api.serializers import DataSerializer

import traceback
import json

@api_view(['GET', 'POST'])
def save_data(request):
    """
    List all data in db, or create a new database entry.
    """
    try:
    	if request.method == 'GET':
    		tasks = Data.objects.all()
    		serializer = DataSerializer(tasks, many=True)
    		return Response(serializer.data)  
    	elif request.method == 'POST':	
    		data = request.data
    		if data.get('message') is None:  #handling message empty case in this case appending the empty string.
    			data = data.copy()
    			data.__setitem__('message',"''")    		
    		serializer = DataSerializer(data=data)
    		if serializer.is_valid():
    			serializer.save()
    			return Response(serializer.data, status=status.HTTP_201_CREATED)
    		else:
        		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    except Exception as e:
    	traceback.print_exc()
    	raise
    
    

