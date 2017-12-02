from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content


class Test(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    default_code = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.content


class Student(models.Model):
    user = models.OneToOneField(User)
    tests_passed = models.ManyToManyField(Topic, default=None, blank=True)
