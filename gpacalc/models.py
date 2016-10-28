from __future__ import unicode_literals

from django.db import models


class College(models.Model):
    collegename = models.CharField(max_length=200, primary_key = True)

class Student(models.Model):
    YEAR_CHOICES = (("FR","Freshman"), ("SO","Sophomore"), ("JU","Junior"), ("SE","Senior+"))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gpa = models.CharField(max_length=3, null=True, blank = True)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20, primary_key = True)
    year = models.CharField(choices = YEAR_CHOICES, max_length=2)
    collegename = models.ForeignKey(College, on_delete=models.PROTECT, null = True, blank = True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def calculateGPA(self):
        vals = CollegeOrganizer.objects.get(username=self.username, collegename = self.collegename)
        classnames = vals.objects.values_list('classname')
        grades = vals.objects.values_list('grade')
        classes = classnames.objects.all().select_related("class")
        credits = []
        for object in classes:
            credits.append(object.credits)
        totalcredits = sum(credits)
        credsxgrades = 0
        for x in range(len(grades)):
            credsxgrades = credsxgrades + (grades[x][0]*credits[x])
        gpa = credsxgrades/totalcredits
        return gpa


class Semester(models.Model):
    SEASON_CHOICES = (("FA","Fall"), ("SP","Spring"), ("SU","Summer"))
    class Meta:
        unique_together = (('season', 'year'),)
    season = models.CharField(choices = SEASON_CHOICES, max_length=2)
    year = models.CharField(max_length=4)

class Class(models.Model):
    name = models.CharField(max_length=20, primary_key=True, null=False)
    credits = models.CharField(max_length=10)

class Grade(models.Model):
    GRADE_CHOICES = ((4.0,"A"), (3.0,"B"), (2.0,"C"), (1.0,"D"), (0.0,"F"))
    grade = models.DecimalField(choices=GRADE_CHOICES, max_digits=2, decimal_places=1)

class CollegeOrganizer(models.Model):
    class Meta:
        unique_together = (('username', 'collegename', 'semestername', 'classname'),)
    username = models.OneToOneField(Student, on_delete=models.PROTECT)
    collegename = models.OneToOneField(College, on_delete=models.PROTECT)
    semestername = models.OneToOneField(Semester, on_delete=models.PROTECT)
    classname = models.OneToOneField(Class, on_delete=models.PROTECT)
    grade = models.OneToOneField(Grade, on_delete=models.PROTECT, null=True)
