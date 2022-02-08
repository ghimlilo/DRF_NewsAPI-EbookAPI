from django.urls import URLPattern, path
from quotes.api.views import QuoteListCreateAPIView, QuoteDetailAPIView

urlpatterns = [
    path("/quotelist", QuoteListCreateAPIView.as_view()),
    path("/quotedetail/<int:pk>", QuoteDetailAPIView.as_view())
]