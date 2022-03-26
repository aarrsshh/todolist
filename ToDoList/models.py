from django.utils.timezone import now
from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now, blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
