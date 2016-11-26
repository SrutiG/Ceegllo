from __future__ import unicode_literals

from django.db import models

import datetime


class College(models.Model):
    collegename = models.CharField(max_length=200, primary_key = True)
    def __str__(self):
        return self.collegename

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

    def __repr__(self):
        return self.username

    def calculateGPA(self):
        vals = PastSemester.objects.filter(username=self.username)
        classnames = PastSemester.objects.filter(username=self.username).values_list('classname', flat=True)
        gradeslist = PastSemester.objects.filter(username=self.username).values_list('grade', flat=True)
        classes = PastSemester.objects.all().select_related("classname")
        credits = []
        grades = []
        for object in gradeslist:
            if object == 1:
                grades.append(4.0)
            elif object == 2:
                grades.append(3.0)
            elif object == 3:
                grades.append(2.0)
            elif object == 3:
                grades.append(1.0)
            elif object == 4:
                grades.append(0.0)
        for object in classes:
            credits.append(int(object.classname.credits))
        totalcredits = sum(credits)
        credsxgrades = 0
        print(grades)
        print(credits)
        for x in range(len(grades)):
            credsxgrades = credsxgrades + (grades[x]*credits[x])
        gpa = float(credsxgrades)/float(totalcredits)
        return gpa

    def getPastSemesters(self):
        semesters = {}
        semesterObjects = PastSemester.objects.all().select_related("semestername").filter(username=self.username)
        for semester in semesterObjects:
            semesters[semester.semestername.__str__] = []
            classObjects = PastSemester.objects.all().select_related("classname")\
                .filter(username=self.username, semestername = semester.semestername)
            for object in classObjects:
                semesters[semester.semestername.__str__].append((object.classname.name, object.classname.credits, object.grade))
        return semesters

    def getFutureSemesters(self):
        semesters = {}
        semesterObjects = FutureSemester.objects.all().select_related("semestername").filter(username=self.username)
        for semester in semesterObjects:
            semesters[semester.semestername.__str__] = []
            classObjects = FutureSemester.objects.all().select_related("classname")\
                .filter(username=self.username, semestername=semester.semestername)
            for object in classObjects:
                semesters[semester.semestername.__str__].append((object.classname.name, object.classname.credits))
        return semesters

    def getCurrentSemester(self):
        semester = {}
        semesterObjects = CurrentSemester.objects.all().select_related("semestername").filter(username=self.username)
        print(semesterObjects)
        print(semesterObjects[0])
        semester[semesterObjects[0].semestername.__str__] = []
        classObjects = CurrentSemester.objects.all().select_related("classname").filter(username=self.username,
                                                                                        semestername=semesterObjects[0].semestername)
        for object in classObjects:
            semester[semesterObjects[0].semestername.__str__].append((object.classname.name, object.classname.credits))
        return semester



class Semester(models.Model):
    SEASON_CHOICES = (("FA","Fall"), ("SP","Spring"), ("SU","Summer"))
    class Meta:
        unique_together = (('season', 'year'),)
    season = models.CharField(choices = SEASON_CHOICES, max_length=2)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.season + " " + self.year

class Class(models.Model):
    name = models.CharField(max_length=20, primary_key=True, null=False)
    credits = models.CharField(max_length=10)
    collegename = models.ForeignKey(College, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Grade(models.Model):
    GRADE_CHOICES = ((4.0,"A"), (3.0,"B"), (2.0,"C"), (1.0,"D"), (0.0,"F"))
    grade = models.DecimalField(choices=GRADE_CHOICES, max_digits=2, decimal_places=1)
    def __str__(self):
        return str(self.grade)

class PastSemester(models.Model):
    class Meta:
        unique_together = (('username', 'collegename', 'semestername', 'classname'),)
    username = models.ForeignKey(Student, on_delete=models.PROTECT)
    collegename = models.ForeignKey(College, on_delete=models.PROTECT)
    semestername = models.ForeignKey(Semester, on_delete=models.PROTECT)
    classname = models.ForeignKey(Class, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.username) + " " + str(self.classname) + " " + str(self.grade)

class CurrentSemester(models.Model):
    class Meta:
        unique_together = (('username', 'semestername', 'classname', 'collegename'),)
    username = models.ForeignKey(Student, on_delete=models.PROTECT)
    collegename = models.ForeignKey(College, on_delete=models.PROTECT)
    semestername = models.ForeignKey(Semester, on_delete=models.PROTECT)
    classname = models.ForeignKey(Class, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.username) + " " + str(self.classname) + " " + str(self.grade)

class FutureSemester(models.Model):
    class Meta:
        unique_together = (('username', 'collegename', 'semestername', 'classname'),)
    username = models.ForeignKey(Student, on_delete=models.PROTECT)
    collegename = models.ForeignKey(College, on_delete=models.PROTECT)
    semestername = models.ForeignKey(Semester, on_delete=models.PROTECT)
    classname = models.ForeignKey(Class, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.username) + " " + str(self.classname)