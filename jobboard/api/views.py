from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from jobboard.models import Joboffer
from jobboard.api.serializers import JobOfferSerializer

class JobBoardListCreateAPIView(APIView):

    def get(self, request):
        joboffers = Joboffer.objects.all()  #filter(active=True)
        serializer = JobOfferSerializer(joboffers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobBoardDetailAPIView(APIView):
        
    def get_object(self, pk):
        joboffer = get_object_or_404(Joboffer, pk=pk)
        return joboffer
    
    def get(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(joboffer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(joboffer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        joboffer = self.get_object(pk)
        joboffer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
