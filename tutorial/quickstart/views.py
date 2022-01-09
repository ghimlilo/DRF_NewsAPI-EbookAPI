from django.contrib.auth.models      import PermissionsMixin, User, Group
from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework                  import viewsets
from rest_framework                  import permissions
from snippets import permissons
from tutorial.quickstart import serializers
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permisson_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permisson_classes = [permissions.IsAuthenticated]
