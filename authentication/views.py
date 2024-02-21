from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class HelloAuthView(GenericAPIView):
    def get(self, request):
        return Response(
            data = {
                'message': 'Hello to Auth View'
            },
            status=status.HTTP_200_OK
        )