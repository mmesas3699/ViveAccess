from django.db import models

from .grade import Grade


class Student(models.Model):
    document = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=80, blank=False, null=False)
    last_name_1 = models.CharField(max_length=80, blank=False, null=False)
    last_name_2 = models.CharField(max_length=80)
    grade = models.ForeignKey(
        Grade,
        on_delete=models.PROTECT,
        related_name='students')

    def __str__(self):
        return f'{self.first_name} {self.last_name_1} {self.grade}'
