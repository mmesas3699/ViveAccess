from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.name}'
