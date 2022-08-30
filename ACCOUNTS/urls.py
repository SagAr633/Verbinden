from django.urls import path
from django import views
from ACCOUNTS import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('logout', views.signout, name='signout'),
    # path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/followers/add', views.AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', views.RemoveFollower.as_view(), name='remove-follower'),
    path('add_pro', views.ProfileAddView.as_view(), name='add_profile'),
    path('all_users', views.AllUsers.as_view(), name='all_users'),
    path('add_posts', views.AddPostView.as_view(), name='add_post'),
    path('my_posts', views.MyPostsView.as_view(), name='my_post'),
    path('all_posts', views.AllPostsView.as_view(), name='all_post'),
    path('user_detail', views.MyDetailView.as_view(), name='user_detail'),
    path('profiles/<int:pk>/', views.OthersProfileView.as_view(), name='other_profile'),
    path('like/<int:post_id>', views.like, name='like'),
    path('pro_update/<int:pk>', views.ProfileUpdateView.as_view(), name='pro_update'),

]
