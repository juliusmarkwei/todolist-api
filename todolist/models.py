from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Task(models.Model):        
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, null=False, on_delete=models.CASCADE, default=1
    )
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    class Meta:
        ordering = ('-created_at')
        
    def __str__(self):
        return self.title
