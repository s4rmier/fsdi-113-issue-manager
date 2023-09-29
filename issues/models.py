from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Issue(models.Model):
    summary = models.CharField(max_length=512)
    description = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee",
        blank=True, null=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )

    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.summary[:256]

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

    def formatted_created_on(self):
        return self.created_on.strftime("%m/%d/%y")
