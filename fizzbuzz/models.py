from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)

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

    def __str__(self):
        return self.content
