from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=4, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'
