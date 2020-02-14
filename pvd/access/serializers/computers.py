from rest_framework import serializers

from access.models import Computer
from .classrooms import ClassroomSerializer


class ComputerSerializer(serializers.ModelSerializer):

    classroom = ClassroomSerializer()

    class Meta:
        model = Computer
        fields = ('name', 'classroom')


class CreateComputerSerializer(serializers.Serializer):
	
	name = serializers.CharField(max_length=5)
	classroom = serializers.CharField(max_length=30)

	def validate(self, data):
		data = self.context['request'].data
		q = Computer.objects.filter(name=data['name'])
		if q.exists():
			raise serializers.ValidationError('A Computer with this name already exists :(.')
		return data

	def create(self, validated_data):
		classroom = self.context['classroom']
					
		# Computer
		computer = Computer.objects.create(
			name=validated_data['name'], 
			classroom=classroom
		)

		return computer
