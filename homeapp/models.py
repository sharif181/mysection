from django.db import models


class quiz(models.Model):
    courseCode = models.CharField(max_length=8)
    courseTitle = models.CharField(max_length=20)
    topic = models.TextField()
    date = models.DateField()
    time = models.TimeField()


class presentation (models.Model):
    courseCode = models.CharField(max_length=8)
    courseTitle = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField(null=True,blank=True)


class assignment(models.Model):
    courseCode = models.CharField(max_length=8)
    courseTitle = models.CharField(max_length=20)
    lastDate = models.DateField()
    comment = models.TextField(null=True,blank=True)

class Announcement(models.Model):
    desc = models.TextField()
    stay = models.DateField()