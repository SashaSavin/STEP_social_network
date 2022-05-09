
from django.urls import path
from .views import ElemsView, \
    ElemView, NeedUpdateView, \
    index, theme, post_like, \
    profile, profiles_list, \
    create_post, upd_profile, \
    del_profile, posts_profile, \
    user_post_delete, subs_view, add_sub, profile_page, get_list_video, get_video, get_streaming_video

urlpatterns = [
    path('', index, name='gallery'),
    path('chat/', ElemsView.as_view()),
    path('post/<int:pk>/', ElemView.as_view(), name='detail'),
    path('edit/<int:pk>', NeedUpdateView.as_view()),
    path('theme/', theme, name='theme'),
    path('post-like/<int:pk>', post_like, name="post_like"),
    path('profile', profile, name='profile'),
    path('profiles', profiles_list, name='profiles'),
    path('profile/<int:pk>', profile_page, name='user_profile'),
    path('edit_profile', upd_profile, name='upd'),
    path('create_post', create_post, name='create'),
    path('all_posts', posts_profile, name='usr_pst'),
    path('delete_profile', del_profile, name='del'),
    path('del_post/<int:pk>/', user_post_delete, name='del_pst'),
    path('show_subs', subs_view, name='show_subs'),
    path('subs/<int:userId>', add_sub, name='subscribe'),

    path('video_stream/<int:pk>/', get_streaming_video, name='stream'),
    path('video/<int:pk>/', get_video, name='video'),
    path('video/', get_list_video, name='home'),

]


