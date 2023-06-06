from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid


class ToDoItem(models.Model):
    
    class ToDoStatus(models.TextChoices):
        OPEN = 'OPEN'
        WORKING = 'WORKING'
        DONE = 'DONE'
        OVERDUE = 'OVERDUE'

    
    todo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    description = models.TextField()
    status = models.TextField(choices=ToDoStatus.choices, default=ToDoStatus.OPEN)
    tag = models.CharField(max_length=10)
    dueDate = models.DateTimeField()
    createdAt = models.DateTimeField()
    