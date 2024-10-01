from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
from .models import Course, Enrollment, Certification

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'course', 'is_completed', 'completion_date')
    list_filter = ('is_completed', 'course')
    readonly_fields = ('enrollment_date',)

    # Overriding the default behavior to hide the completion date field
    def get_fields(self, request, obj=None):
        fields = ['student_name', 'course', 'is_completed']
        if obj and obj.is_completed:
            fields.append('completion_date')
        return fields

    # Adding custom JavaScript to handle dynamic hiding/showing of fields in the admin interface
    class Media:
        js = ('admin/js/enrollment.js',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'duration', 'filter_button')  # Add filter_button here

    def filter_button(self, obj):
        # Generate the URL for the filter page
        url = reverse('filter_courses')
        # Return HTML for a button
        return format_html(f'<a class="button" href="{url}">Filter Courses</a>')

    filter_button.short_description = 'Filter Courses'
    filter_button.allow_tags = True

admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Course)
#admin.site.register(Enrollment)
admin.site.register(Certification)