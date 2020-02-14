from rest_framework import mixins, viewsets

from access.models import Classroom
from access.serializers import ClassroomSerializer


class ClassroomViewSet(mixins.ListModelMixin, 
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):

    serializer_class = ClassroomSerializer
    lookup_field = 'name'
    queryset = Classroom.objects.all()
