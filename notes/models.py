from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Category(models.TextChoices):
    PERSONAL = 'PER', 'Personal'
    WORK = 'WRK', 'Work'
    STUDY = 'STU', 'Study'
    OTHER = 'OTH', 'Etc'

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Name")
    text = models.TextField(verbose_name="Note text", null=True, blank=True)
    reminder = models.DateTimeField(null=True, blank=True, verbose_name="Reminder")
    category = models.CharField(
        max_length=3,
        choices=Category.choices,
        default=Category.OTHER,
        verbose_name="Category",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_edit', kwargs={'pk': self.pk})