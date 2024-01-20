from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
import requests
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


class Commends(models.Model):
    post=models.ForeignKey(POST,on_delete=models.CASCADE)
    Commends=models.CharField(max_length=100)
    user=models.ForeignKey(profile,on_delete=models.CASCADE)
    update_date=models.DateField(auto_now=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} commended on post{self.post}"

class Like_Post(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)
    def __str__(self):
        return self.username
class Favorate_POST(models.Model):
    post=models.ForeignKey(POST,on_delete=models.CASCADE)
    user=models.ForeignKey(profile,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
class Followers(models.Model):
    user = models.CharField(max_length=100)
    follower =models.CharField(max_length=100)

    def __str__(self):
        return self.user
# online virtual resume
class Professional_Profile(models.Model):
    normal_profile=models.ForeignKey(profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    objectives=models.TextField()
    last_name=models.CharField(max_length=100,blank=True,null=True)
    profimg=models.ImageField(upload_to='prof_images',default=None)
    number=models.BigIntegerField()
    location=models.CharField(max_length=200,null=True,blank=True)
    website=models.URLField(max_length=200,null=True,blank=True)
    def __str__(self):
        return f"{self.name}'s Professional Pofile"
    def save(self, *args, **kwargs):
        # Set the default value for profimg to the profileimg of normal_profile
        if not self.profimg:
            self.profimg = self.normal_profile.profileimg
        super().save(*args, **kwargs)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies_used = models.CharField(max_length=255)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    project_url=models.CharField(max_length=200,blank=True,null=True)
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)
    #uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.title

class Internship(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
# resume/models.py
from django.db import models

class Skill(models.Model):
    SKILL_LEVELS = [
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    skill_name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=SKILL_LEVELS, default='Intermediate')
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.skill_name} - {self.level}"

class Hobbies(models.Model):
     hobbie_name=models.CharField(max_length=200)
     profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)

     def __str__(self) -> str:
         return  f"{self.hobbie_name}"
class Social_Media_URLS(models.Model):
    website_name=models.CharField(max_length=200)
    link=models.URLField(max_length=200)
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.website_name} url"
class Soft_Skill(models.Model):
    SKILL_LEVELS = [
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    skill_name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=SKILL_LEVELS, default='Intermediate')
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.skill_name} - {self.level}"
class Education(models.Model):
    institute=models.CharField(max_length=200)
    degree=models.CharField(max_length=100,default="EX: Bechelor's")
    field_of_study=models.CharField(max_length=200 ,default="EX: Business")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    percentage=models.FloatField()
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.institute

class Certification(models.Model):
    certificate_name=models.CharField(max_length=200)
    organization=models.CharField(max_length=200)
    cert_img=models.ImageField(upload_to='cert_image',null=True,blank=True)
    issue_date=models.DateField(blank=True,null=True)
    expiry_date=models.DateField(blank=True,null=True)
    credential_id=models.CharField(max_length=200 ,null=True,blank=True)
    credential_url=models.CharField(max_length=200 ,null=True,blank=True)
    skills=models.CharField(max_length=100,null=True,blank=True)
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)
    as_post=models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.profile.normal_profile.user} added certificate {self.certificate_name}"

class Achivements(models.Model):
    title=models.CharField(max_length=200)
    ACHIVEMENT_LEVEL=[
        ('First','First'),
        ('Second','Second'),
        ('Third','Third'),
        ('Participation','Participation')
    ]
    place=models.CharField(choices=ACHIVEMENT_LEVEL,default="Participation",max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='Achive_images',null=True,blank=True)
    skill=models.CharField(max_length=200)
    date=models.DateField(blank=True,null=True)
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)
    as_post=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
class Languages(models.Model):
    language=models.CharField(max_length=200)
    LANGUAGE_LEVEL=[
       ('Elementery Proficiency','Elementery Proficiency'),
       ('Limited working Proficiency','Limited working Proficiency'),
       ('Professional working Proficiency','Professional working Proficiency'),
       ('Full Professional  Proficiency','Full Professional  Proficiency'),
       ('Native or bilingual Proficiency','Native or bilingual Proficiency')
    ]
    level=models.CharField(choices=LANGUAGE_LEVEL,default="read",max_length=200)
    profile=models.ForeignKey(Professional_Profile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.language
