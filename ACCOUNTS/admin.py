from django.contrib import admin
from ACCOUNTS.models import Post, UserProfile

admin.site.register(UserProfile)
admin.site.register(Post)
