from rest_framework import mixins, viewsets
from rest_framework.response import Response

from access.models import Access, Student
from access.serializers import StudentSerializer, AccessSerializer


class StudentViewSet(mixins.ListModelMixin,
					 mixins.CreateModelMixin,
					 mixins.RetrieveModelMixin,
					 viewsets.GenericViewSet):

	serializer_class = StudentSerializer
	lookup_field = 'document'
	queryset = Student.objects.all()

	def retrieve(self, request, pk=None, *args, **kwargs):
		student = self.get_object()
		access =  Access.objects.filter(student=student)

		data = {'student': StudentSerializer(student).data, 'access':AccessSerializer(access, many=True).data }

		return Response(data)
