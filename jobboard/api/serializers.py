from dataclasses import fields
from rest_framework import serializers
from jobboard.models import Joboffer


class JobOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Joboffer
        fields = "__all__"