from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializers

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    

def index(request):
    return render(request, 'index.html', {})


