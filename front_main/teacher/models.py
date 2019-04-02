from django.db import models

# Create your models here.

class Teacher(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    branch = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'