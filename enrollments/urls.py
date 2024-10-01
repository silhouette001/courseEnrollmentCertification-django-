from django.urls import path
from .views import CourseListCreateView, EnrollmentListCreateView, EnrollmentDetailView, CertificationListCreateView
from .views import home
from . import views

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-detail'),
    path('certifications/', CertificationListCreateView.as_view(), name='certification-list-create'),
    path('filter/', views.filter_courses, name='filter_courses'),
    path('', home, name='home'),
]
