from django.contrib import admin

# Register your models here.
from .models import profile,POST,Like_Post,Followers,Professional_Profile,HashTags
admin.site.register(profile)
admin.site.register(POST)
admin.site.register(Like_Post)
admin.site.register(Followers)
admin.site.register(Professional_Profile)
admin.site.register(HashTags)