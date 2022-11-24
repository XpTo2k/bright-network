from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    followees = models.ManyToManyField(
        'User', blank=True, related_name='followe')
    followers = models.ManyToManyField(
        'User', blank=True, related_name='follower')

    def __str__(self):
        return f"{self.username}"

    def serialize(self):
        return {
            "id": self.id,
            "user": self.username,
            "first": self.first_name,
            "last": self.last_name,
            "email": self.email,
            "joined": self.date_joined.strftime("%b %d %Y, %I:%M %p"),
            "followees": [user.id for user in self.followees.all()],
            "followers": [user.id for user in self.followers.all()],
        }


class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024)
    replies = models.ManyToManyField('self')
    upvotes = models.ManyToManyField(User, blank=True, related_name="upvoter")
    downvotes = models.ManyToManyField(
        User, blank=True, related_name="downvoter")
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id}: {self.commenter}"


class Ideas(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    idea = models.CharField(max_length=2048)
    comments = models.ManyToManyField(Comments, blank=True)
    bright = models.ManyToManyField(User, blank=True, related_name="bright")
    dark = models.ManyToManyField(User, blank=True, related_name="dark")
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(default=timezone.now)

    @property
    def lumen(self):
        lumen = len(self.bright.all()) - len(self.dark.all())
        return lumen

    def __str__(self):
        return f"{self.id}: {self.title}"

    def serialize(self):
        return {
            "id": self.id,
            "author": self.author.id,
            "idea": self.idea,
            "comments": [comment.id for comment in self.comments.all()],
            "bright": [user.id for user in self.bright.all()],
            "dark": [user.id for user in self.dark.all()],
            "created": self.created.strftime("%b %d %Y, %I:%M %p"),
            "edited": self.edited.strftime("%b %d %Y, %I:%M %p"),
            "lumen": self.lumen
        }
