from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20, blank=True, null=True)
    section = models.CharField(max_length=5, blank=True, null=True)
    branch = models.CharField(max_length=5, blank=True, null=True)
    batch = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
    	return self.name