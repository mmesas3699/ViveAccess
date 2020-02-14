from rest_framework import serializers

from access.models import Accessory


class AccessorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Accessory
        fields = ('id', 'name',)
