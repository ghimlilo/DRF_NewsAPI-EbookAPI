from django.urls import URLPattern, path
from profiles.api.views import ProfileList

urlpatterns = [
    path("/profiles", ProfileList.as_view())
]