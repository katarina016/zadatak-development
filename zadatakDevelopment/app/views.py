from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer

class DataModelViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataListCreateView(generics.ListCreateAPIView, TemplateView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataListView(APIView):
    def get(self, request, *args, **kwargs):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        context = {'data': serializer.data}
        return render(request, 'index.html', context)