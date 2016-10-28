from django.contrib import admin

from .models import CollegeOrganizer
from .models import Student

admin.site.register(CollegeOrganizer)
admin.site.register(Student)