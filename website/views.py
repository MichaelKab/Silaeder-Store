from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.http import Http404
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
def Main(request):
    html = "<html><body> Страница </body></html>"
    return HttpResponse(html)

def UserData_v(request, ID):
    UserData = Session_log.objects.get(user_id=ID)
    html = "<html><body>{}</body></html>".format(UserData)
    return UserData

def Transaction_v(request, ID):
    Transaction = Session_log.objects.get(id_user=ID)
    html = "<html><body>{}</body></html>".format(Transaction)
    return Transaction

def Product_v(request, ID):
    Product = Session_log.objects.get(name_product=ID)
    html = "<html><body>{}</body></html>".format(Product)
    return Product

def Session_log_v(request, ID):
    session = Session_log.objects.get(id_user =ID )
    html = "<html><body>{}</body></html>".format(session)
    return session