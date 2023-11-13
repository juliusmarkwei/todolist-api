from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
import re


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class EndUsers(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, related_name="endusers"
    )
    email = models.EmailField(default=None, blank=True)
    joined_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.user.email

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "End Users"
        verbose_name_plural = "End Users"


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
        now = timezone.now().strftime("%d-%m-%Y %I:%M %p")
        now_datetime = datetime.strptime(now, "%d-%m-%Y %I:%M %p")
        str_formatted_due_date = self.due_date.strftime("%d-%m-%Y %I:%M %p")
        formatted_due_date = datetime.strptime(
            str_formatted_due_date, "%d-%m-%Y %I:%M %p"
        )

        time_difference = formatted_due_date - now_datetime
        print(str(time_difference), f"and the type is {type(time_difference)}")

        match = re.match(r'(?:(\d+) day(?:s)?, )?(\d+):(\d+):(\d+)', str(time_difference))
        if match:
            days = int(match.group(1) or 0)  # If days are not present, default to 0
            hours = int(match.group(2))
            minutes = int(match.group(3))
            seconds = int(match.group(4))
        print('Countdown matched')

        self.countdown = (
            f"{days} day(s), {hours} hour(s),  {minutes} minute(s), {seconds} seconds"
        )

    def save(self, *args, **kwargs):
        self.calculate_countdown()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
