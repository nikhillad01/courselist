from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Course
        fields = "__all__"
