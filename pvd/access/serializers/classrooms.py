from rest_framework import serializers

from access.models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ('name',)
