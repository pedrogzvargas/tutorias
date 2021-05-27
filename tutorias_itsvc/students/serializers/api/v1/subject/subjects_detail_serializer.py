from rest_framework import serializers


class SubjectsDetailSerializer(serializers.Serializer):
    taking_subjects = serializers.IntegerField()
    approved_subjects = serializers.IntegerField()
    failed_subjects = serializers.IntegerField()
    approved_subjects_points = serializers.IntegerField()
    taking_subjects_points = serializers.IntegerField()
    total_points = serializers.IntegerField()
