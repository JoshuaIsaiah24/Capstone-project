from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializers, BookingSerializers

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    
    
def index(request):
    return render(request, 'index.html', {})


