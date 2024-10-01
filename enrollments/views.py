from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from .models import Course, Enrollment, Certification
from .serializers import CourseSerializer, EnrollmentSerializer, CertificationSerializer
from django.utils.dateparse import parse_date


def home(request):
    return HttpResponse("<h1>Welcome to the Course Enrollment System</h1>")


# Create your views here.
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class CertificationListCreateView(generics.ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer


def filter_courses(request):

    # Start with all courses
    courses = Course.objects.all()
    

    # Extract query parameters from request
    category = request.GET.get('category', None)
    enrollment_date = request.GET.get('enrollment_date', None)
    is_completed = request.GET.get('is_completed', None)

    courses = Course.objects.all().prefetch_related('enrollments') 
    #courses = Course.objects.all()
    


    # Filter by category if provided
    if category:
        courses = courses.filter(category__iexact=category)

    # Filter by enrollment date if provided
    if enrollment_date:
        # Convert string date to a proper date object
        enrollment_date = parse_date(enrollment_date)
        courses = courses.filter(enrollment__enrollment_date=enrollment_date)

    # Filter by completion status if provided
    if is_completed is not None:
        # Convert string 'true'/'false' to a boolean
        is_completed = is_completed.lower() == 'true'
        courses = courses.filter(enrollment__is_completed=is_completed)

   
    # Construct a response with the filtered data
    result = [
        {
            "course_name": course.title,
            "category": course.category,
            "duration": course.duration,
            
        }
        for course in courses
    ]

    # Return filtered results as a JSON response
    return JsonResponse(result, safe=False)