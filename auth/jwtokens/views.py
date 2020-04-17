from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        content = {
            'message':' Response One'
        }
        return Response(content, status=status.HTTP_200_OK)

# Create your views here.
