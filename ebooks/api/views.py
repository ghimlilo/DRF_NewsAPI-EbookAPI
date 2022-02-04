from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from ebooks.api.permissions import IsAdminUserOrReadonly, IsReviewAuthorOrReadOnly

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadonly]

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadonly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
        review_author = self.request.user
        
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)

        if review_queryset.exists:
            raise ValidationError("You Have Already Reviewd This Ebook!")

        serializer.save(ebook = ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

# class EbookListCreateAPIView(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                             generics.GenericAPIView):
    
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)