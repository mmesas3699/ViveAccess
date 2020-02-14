from rest_framework import serializers

from access.models import Grade


class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('name',)