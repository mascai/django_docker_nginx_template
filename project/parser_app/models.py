from django.db import models


class BaseTask(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) # True - task is running
    data = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name