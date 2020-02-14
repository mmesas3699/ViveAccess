from django.db import models

from .classroom import Classroom


class Computer(models.Model):
    name = models.CharField(max_length=5, primary_key=True)
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.CASCADE,
        related_name='computers')

    def __str__(self):
        return f'{self.name} / {self.classroom}'
