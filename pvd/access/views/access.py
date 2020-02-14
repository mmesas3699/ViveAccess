from rest_framework import mixins, viewsets

from access.models import Access
from access.serializers import AccessSerializer, CreateAccessSerializer


class AccessViewSet(mixins.ListModelMixin,
					mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.CreateModelMixin,
	                viewsets.GenericViewSet):

    queryset = Access.objects.all()

    def get_serializer_class(self):
    	if self.action == 'create':
    		return CreateAccessSerializer

    	return AccessSerializer
