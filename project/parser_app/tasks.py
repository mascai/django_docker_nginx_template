import requests
import time

from datetime import datetime
from parser_app.models import BaseTask
from core_app.celery import app

from django.core.cache import cache


def parse_quotes(celery_task_id: str):
    response = requests.get("https://quotes.toscrape.com/")
    if response.status_code == 200:
        new_task = BaseTask.objects.create(
            name=celery_task_id,
            data=response.content,
        )
        new_task.save()
        

@app.task(name='create_task', bind=True)
def create_task(self, task_type):
    parse_quotes(self.request.id)
    return True
