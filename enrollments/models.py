from django.db import models
from django.utils import timezone


# Create your models here.

# Model for Courses
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in hours")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.duration} hours"

# Model for Enrollments
class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    enrollment_date = models.DateField(default=timezone.now)  
    is_completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically set the completion date when the course is marked as completed
        if self.is_completed and not self.completion_date:
            self.completion_date = timezone.now()
        elif not self.is_completed:
            self.completion_date = None    
        super().save(*args, **kwargs)

    def __str__(self):
        # Handle None for enrollment_date and completion_date safely
        if self.enrollment_date:
            enrollment_date_str = self.enrollment_date.strftime('%Y-%m-%d')
        else:
            enrollment_date_str = 'No Enrollment Date'

        if self.completion_date:
            completion_date_str = self.completion_date.strftime('%Y-%m-%d')
        else:
            completion_date_str = 'Not Completed'

        return f"{self.student_name} - Enrolled on: {enrollment_date_str}, Completed: {completion_date_str}"

# Model for Certifications
class Certification(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Access the related enrollment and course information
        student_name = self.enrollment.student_name
        course_title = self.enrollment.course.title
        course_duration = self.enrollment.course.duration  # Get course duration
        completion_date = self.enrollment.completion_date  # Get completion date

        # Safely handle None completion_date
        if completion_date:
            completion_date_str = completion_date.strftime('%Y-%m-%d')
        else:
            completion_date_str = 'No Completion Date'

        return (
            f"Certification for {student_name} for completing {course_title} "
            f"({course_duration} hours) on {completion_date_str}"
        )