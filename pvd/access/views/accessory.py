from rest_framework import mixins, viewsets

from access.models import Accessory
from access.serializers import AccessorySerializer


class AccessoryViewSet(mixins.ListModelMixin, 
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = AccessorySerializer
    lookup_field = 'id'
    queryset = Accessory.objects.all()
