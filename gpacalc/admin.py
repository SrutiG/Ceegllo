from django.contrib import admin

from .models import CollegeOrganizer
from .models import Student
from .models import College
from .models import Class
from .models import Semester
from .models import Grade

admin.site.register(CollegeOrganizer)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(College)
admin.site.register(Semester)
admin.site.register(Grade)