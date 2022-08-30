from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ACCOUNTS.models import UserProfile, Post, Likes
from ACCOUNTS.forms import ProfileForm, PostForm
from USERS.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


class HomeView(TemplateView):
    template_name = 'home.html'


class ProfileAddView(CreateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'profile_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AllUsers(ListView):
    model = User
    template_name = 'all_users.html'
    context_object_name = 'all_users'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('my_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MyPostsView(ListView):
    model = Post
    template_name = 'my_posts.html'
    context_object_name = 'my_posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class AllPostsView(ListView):
    model = Post
    template_name = 'all_posts.html'
    context_object_name = 'all_posts'


def signout(request):
    logout(request)
    return redirect('login')


class OthersProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_date')
        followers = profile.followers.all()
        for follower in followers:
            global is_following
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False
        number_of_followers = len(followers)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'is_following': is_following,
            'number_of_followers': number_of_followers,
        }

        return render(request, 'others_profile.html', context)


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)
        return redirect('other_profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        return redirect('other_profile', pk=profile.pk)


def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()
    if not liked:
        liked = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        liked = Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse('all_post'))


class MyDetailView(TemplateView):
    template_name = 'user_detail.html'


class ProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('user_detail')
