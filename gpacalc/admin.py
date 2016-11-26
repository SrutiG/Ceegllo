from django.contrib import admin

from .models import PastSemester
from .models import FutureSemester
from .models import CurrentSemester
from .models import Student
from .models import College
from .models import Class
from .models import Semester
from .models import Grade

admin.site.register(PastSemester)
admin.site.register(FutureSemester)
admin.site.register(CurrentSemester)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(College)
admin.site.register(Semester)
admin.site.register(Grade)