from django.shortcuts import get_object_or_404

from rest_framework import serializers

from access.models import Grade, Student
from .grades import GradeSerializer


class StudentSerializer(serializers.ModelSerializer):

	grade = GradeSerializer()
	
	class Meta:
		model = Student
		fields = ['first_name', 'last_name_1', 'last_name_2', 'document', 'grade']

	def validate(self, data):
		""" Verify if Grade exists."""

		data = self.initial_data
		try:
			grade = Grade.objects.get(name=data['grade']['name'])
		except Grade.DoesNotExist:
			raise serializers.ValidationError('Grade does not exists.!!')

		data['grade'] = grade
		return data

	def create(self, validated_data):
		student = Student.objects.create(
			document=validated_data['document'],
			first_name=validated_data['first_name'],
			last_name_1=validated_data['last_name_1'],
			last_name_2=validated_data['last_name_2'],
			grade=validated_data['grade'])

		return student
