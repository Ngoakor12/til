from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Topic(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Record(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField(max_length=250)
    text = models.TextField(blank=True)
    topics = models.ManyToManyField(Topic)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
