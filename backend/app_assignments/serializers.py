from rest_framework import serializers
from .models import Assignment, Hint

class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    assignment_hints = HintSerializer(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = (
            'pk',
            'description',
            'created',
            'assignment_hints',
        )
