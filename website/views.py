from django.shortcuts import render
from django.http import HttpResponse
'''
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from website.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")