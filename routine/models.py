from django.db import models

choice_day=(
    ('saturday','Saturday'),
    ('sunday','Sunday'),
    ('monday','Monday'),
    ('tuesday','Tuesday'),
    ('wednesday','Wednesday'),
    ('thursday','Thursday'),
    ('extra','Extra'),
)


class Routine(models.Model):
    day = models.CharField(max_length=12,choices=choice_day)
    slot = models.TimeField()
    courseTitle = models.CharField(max_length=50)
    teacherIni = models.CharField(max_length=20)
    room = models.CharField(max_length=10)
    
    def __str__(self):
        return self.day
    


