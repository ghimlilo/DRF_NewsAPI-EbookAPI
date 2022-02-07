from django.urls    import URLPattern, path
from jobboard.api.views   import JobBoardListCreateAPIView, JobBoardDetailAPIView

urlpatterns = [
    path("/joboffer", JobBoardListCreateAPIView.as_view()),
    path("/jobofferdetails/<int:pk>", JobBoardDetailAPIView.as_view())
]