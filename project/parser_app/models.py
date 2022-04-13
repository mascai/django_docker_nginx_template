from django.db import models


class BaseTask(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField() # True - task is running