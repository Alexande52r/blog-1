from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

class PublishmentManager(models.Manager):
    def quary_set(self):
        return super().get_quaryest().filter(status= Post.Status.PUBLISHED)

class Post(models.Model):

    class Status(models.TextChoices):
        DRAWT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAWT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")

    objects = models.Manager()
    published = PublishmentManager()

    class Meta:
        ordering = ["-publish"]
    indexes = (
        models.Index(fields=["-publish"])
    )

    def __str__(self):
        return self.title