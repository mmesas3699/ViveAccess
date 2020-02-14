from django.db import models

from .accessory import Accessory
from .computer import Computer
from .student import Student

from users.models import User


class Access(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='access'
    )
    date = models.DateField(auto_now=True)
    entry = models.TimeField(auto_now=True)
    departure = models.TimeField(null=True, blank=True)
    computer = models.ForeignKey(
        Computer,
        on_delete=models.PROTECT,
        related_name='access'
    )
    accessory = models.ForeignKey(
        Accessory,
        on_delete=models.PROTECT,
        related_name='access', null=True
    )
    observation = models.TextField(blank=True)

    def __str__(self):
        return f'{self.date} | {self.computer} {self.student}, ingreso: {self.entry}'
