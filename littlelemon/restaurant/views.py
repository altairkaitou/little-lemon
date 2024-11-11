from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, permissions
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

def index(request):
    return render(request, 'index.html', {})