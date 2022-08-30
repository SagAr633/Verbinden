from django import forms
from ACCOUNTS.models import UserProfile, Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'followers')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'likes')
