from django.contrib import admin

# Register your models here.
from .models import profile,POST,Like_Post
admin.site.register(profile)
admin.site.register(POST)
admin.site.register(Like_Post)