from rest_framework import mixins, viewsets

from access.models import Grade
from access.serializers import GradeSerializer


class GradeViewSet(mixins.ListModelMixin, 
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = GradeSerializer
    lookup_field = 'name'
    queryset = Grade.objects.all()
