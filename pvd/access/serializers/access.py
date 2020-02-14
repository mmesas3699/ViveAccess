from rest_framework import serializers

from access.models import Access, Accessory, Computer, Student
from access.serializers import ComputerSerializer, StudentSerializer


class AccessSerializer(serializers.ModelSerializer):

	student = StudentSerializer()
	computer = ComputerSerializer

	class Meta:
		model = Access
		fields = ['id',
		          'date',
		          'entry',
		          'departure',
		          'computer',
				  'student',
		          'accessory', 
		          'observation']


class CreateAccessSerializer(serializers.ModelSerializer):

	student_id = serializers.CharField(max_length=10) # Student.document
	computer = serializers.CharField(max_length=5)

	class Meta:
		model = Access
		fields = ['observation', 'student_id', 'accessory', 'computer']

	def validate(self, data):
		data = self.initial_data

    	# Queries
		student = Student.objects.filter(document=data['student_id'])
		computer = Computer.objects.filter(name=data['computer'])
		accessory = data.get('accessory')

		# Verify Student
		if not student.exists():
			raise serializers.ValidationError('Student does not exists. :(')

		data['student'] = student[0]

		# Verify Computer
		if not computer.exists():
			raise serializers.ValidationError('Computer does not exists. :(')

		data['computer'] = computer[0]

		# Check if accessory data is sent. If so, it checks the object.
		if accessory:
			q = Accessory.objects.filter(id=accessory)
			if not q.exists():
				raise serializers.ValidationError('Accessory does not exists. :(')
			
			data['accessory'] = q[0]

		return data
