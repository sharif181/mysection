from django.db import models


class quiz(models.Model):
    courseCode = models.CharField(max_length=8)
    courseTitle = models.CharField(max_length=50)
    topic = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.courseTitle


class presentation (models.Model):
    courseCode = models.CharField(max_length=8)
    courseTitle = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.courseTitle


class assignment(models.Model):
    courseCode = models.CharField(max_length=8)
    courseTitle = models.CharField(max_length=50)
    lastDate = models.DateField()
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.courseTitle

class Announcement(models.Model):
    desc = models.TextField()
    stay = models.DateField()