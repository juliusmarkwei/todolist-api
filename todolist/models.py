from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default=None, blank=True)
    joined_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Set the email field to the associated user's email when saving
        self.email = self.user.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    class TaskObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="inprogress")

    options = (
        ("draft", "Draft"),
        ("inprogress", "In progress"),
        ("completed", "Completed"),
    )

    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, null=False, on_delete=models.CASCADE, default=1
    )
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    due_date = models.DateTimeField(null=True, blank=True)
    countdown = models.DurationField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False, default=timezone.now)
    updated_at = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True
    )
    status = models.CharField(max_length=10, choices=options, default="draft")

    def save(self, *args, **kwargs):
        # Check if due_date is set and is a valid datetime object
        if self.due_date and isinstance(self.due_date, timezone.datetime):
            now = timezone.now()
            time_difference = self.due_date - now
            self.countdown = time_difference
        else:
            print("Date mighthave an error")
            self.countdown = None

        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
