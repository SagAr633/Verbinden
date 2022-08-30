from django.db import models
from USERS.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures/', default='uploads/profile_pictures/default.png',
                                blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    # @property
    # def is_following(self):
    #     return self.followers == self.followers
    #
    # def not_following(self):
    #     return self.followers != self.followers


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    caption = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    video = models.FileField(upload_to='post_videos', null=True, blank=True)
    likes = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.caption


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
