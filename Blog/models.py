from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime

# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=140)
    content = models.TextField()
    timeStamps = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamps = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + '...' + ' by ' + self.user.username
