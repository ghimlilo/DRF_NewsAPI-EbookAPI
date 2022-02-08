from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from quotes.api.permissions import IsAdminUserOrReadonly

from quotes.models import Quote
from quotes.api.pagination import SmallSetPagination
from quotes.api.serializers import QuoteSerializer


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("id")
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadonly]
    pagination_class = SmallSetPagination

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadonly]
