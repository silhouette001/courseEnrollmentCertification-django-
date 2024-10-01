from rest_framework import serializers
from .models import Course, Enrollment, Certification  # Adjust based on your model names

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # You can specify specific fields here if needed

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'course', 'student_name', 'enrollment_date', 'is_completed', 'completion_date']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Only include completion_date if is_completed is True
        if not instance.is_completed:
            representation.pop('completion_date', None)
        return representation


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'
