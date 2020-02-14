from django.shortcuts import get_object_or_404

from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from access.models import Computer, Classroom
from access.serializers import ComputerSerializer, CreateComputerSerializer


class ComputerViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = ComputerSerializer
    lookup_field = 'name'
    queryset = Computer.objects.all()
    
    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == 'create':
            return CreateComputerSerializer

        return ComputerSerializer
    
    def create(self, request, *args, **kwargs):
        """Handle computer creation."""
        classroom = get_object_or_404(Classroom, name=request.data['classroom'])
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(
            data=request.data,
            context={'classroom': classroom, 'request': request})
        serializer.is_valid(raise_exception=True)
        computer = serializer.save()
        data = self.get_serializer(computer).data

        return Response(data, status=status.HTTP_201_CREATED)
