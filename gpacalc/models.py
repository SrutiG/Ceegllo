from __future__ import unicode_literals

from django.db import models

class College(models.model):
    gpaDict = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}

    name = models.CharField(max_length=200)

