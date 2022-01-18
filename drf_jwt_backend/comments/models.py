from django.db import models
from drf_jwt_backend.authentication.views import User

class Comments(models.Model):
    user = models.ForeignKey(User)
    video_id = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class Reply(models.Models):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(User)
    text = models.CharField(max_length=50)