from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class EndUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(default=None, blank=True)
    joined_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.user.email

        return super().save(*args, **kwargs)

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
    countdown = models.CharField(max_length=50, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False, default=timezone.now)
    last_update = models.DateTimeField(
        auto_now_add=False, auto_now=False, blank=True, null=True
    )
    status = models.CharField(max_length=10, choices=options, default="draft")
    taskobjects = TaskObject()
    objects = models.Manager()

    def calculate_countdown(self):
        now = timezone.now()

        due_date_utc = self.due_date.astimezone(timezone.utc)
        now_utc = now.astimezone(timezone.utc)

        time_difference = due_date_utc - now_utc

        print(f"The time difference : {time_difference}")
        print(f"The due date from the db : {due_date_utc}")
        print(f"Now date is : {now_utc}")
        days, seconds = divmod(time_difference.seconds, 86400)
        hours, _ = divmod(seconds, 3600)
        countdown_str = f"{days} days, {hours} hours"

        self.countdown = countdown_str

    def save(self, *args, **kwargs):
        self.calculate_countdown()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
