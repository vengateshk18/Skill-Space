from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
User=get_user_model()
# Create your models here.
class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg=models.ImageField(upload_to='profile_images',default="blank_profile_pic.png")
    location=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.username


class POST(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(profile, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post_images')
    caption = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    no_of_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user)


# class Commends(models.Model):
#     post=models.ForeignKey(POST,on_delete=models.CASCADE)
#     Commends=models.CharField(max_length=100)
#     user=models.ForeignKey(profile,on_delete=models.CASCADE)
#     update_date=models.DateField(auto_now=True)
#     created_date=models.DateTimeField(auto_now_add=True)
class Like_Post(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)


    def __str__(self):
        return self.username