from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customers
from django.http import Http404
from .serializers import CustomerSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate

class CustomerView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            try:
                result = Customers.objects.get(pk=pk)
                serializers = CustomerSerializer(result)
                return Response({'status': 'success', "customers": serializers.data}, status=status.HTTP_200_OK)
            except Customers.DoesNotExist:
                raise Http404("Customer does not exist")
        else:
            result = Customers.objects.all()
            serializers = CustomerSerializer(result, many=True)
            return Response({'status': 'success', "customers": serializers.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        result = Customers.objects.get(pk=pk)
        serializer = CustomerSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, pk=None):
        result = get_object_or_404(Customers, pk=pk)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})
