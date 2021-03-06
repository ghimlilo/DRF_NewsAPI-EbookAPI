from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from jobboard.models import JobOffer
from jobboard.api.serializers import JobOfferSerializer

class JobBoardListCreateAPIView(APIView):

    def get(self, request):
        job = JobOffer.objects.filter(available = True) 
        serializer = JobOfferSerializer(job, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobBoardDetailAPIView(APIView):
        
    def get_object(self, pk):
        joboffer = get_object_or_404(JobOffer, pk=pk)
        return joboffer
    
    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobOfferSerializer(job)
        return Response(serializer.data)
    
    def put(self, request, pk):
        job = self.get_object(pk)
        serializer = JobOfferSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
