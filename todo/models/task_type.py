from django.db import models

class TaskType(models.Model):
    """A model of task type"""
    name = models.CharField("Task type", max_length=200, help_text="Enter task type")
    description = models.TextField("Description", max_length=400, help_text="Enter task type description")
