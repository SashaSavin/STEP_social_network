from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from app.models import Post, Theme, Category, Profile
from .forms import ProfileModelForm, PostModelForm
from .mixins import AdminAuthMixin
from django.contrib import messages


def index(request):
    user = request.user
    category = request.GET.get('category')

    if Theme.objects.filter(user=user.username).exists():
        color = Theme.objects.get(user=user.username).color
    else:
        color = 'blue'

    last_posts = Post.objects.all().order_by('-id')[:3]
    popular = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:3]
    cat = Category.objects.all()

    if category == None:
        post = Post.objects.all()

    else:
        post = Post.objects.filter(
            category__name=category)

    context = {'category': cat,
               'color': color,
               'post':post,
               'last_posts': last_posts,
               'popular': popular}

    return render(request, 'index.html', context)


def theme(request):
    color = request.GET.get('color')
    if color == 'dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme = Theme.objects.get(user=request.user.username)
            user_theme.user = request.user.username
            user_theme.color = 'grey'
            user_theme.save()
        else:
            user2 = Theme(user=request.user.username, color='grey')
            user2.save()

    elif color == 'light':
        if Theme.objects.filter(user=request.user.username).exists():
                user_theme1 = Theme.objects.get(user=request.user.username)
                user_theme1.user = request.user.username
                user_theme1.color = 'white'
                user_theme1.save()
        else:
            user4 = Theme(user=request.user.username, color='white')
            user4.save()
    return redirect('/')


def post_like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect('/')



class NeedUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = 'title', 'text'
    success_url = '/'

    def form_valid(self, form):
        messages.success(self.request, "Current data was updated!")
        return HttpResponseRedirect(self.get_success_url())


class ElemsView(ListView):
    model = Post
    template_name = 'chat.html'
    context_object_name = 'post'


class ElemView(AdminAuthMixin, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile }
    return render(request, 'profile.html', context)

def upd_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
           form.save()
        return redirect('/')

    context = {
               'form': form}
    return render(request, 'profile_edit.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles.html', context)


def del_profile(request):
    profile = Profile.objects.get(user=request.user)
    profile.delete()
    return redirect('/')


def posts_profile(request):
    posts = Post.objects.filter(author = request.user).order_by('-id')
    context = {'posts': posts}
    return render(request, 'posts.html', context)


def user_post_delete(request, pk):
    post = Post.objects.get(author = request.user, id=pk)
    post.delete()
    return redirect('/')


def create_post(request):
    form = PostModelForm(request.POST, request.FILES)
    form.instance.author = request.user
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
               'form': form}
    return render(request, 'create_post.html', context)


def subs_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'subscribers.html', context)

def add_sub(request, userId):
    profile = request.user
    sub = Profile.objects.get(id=userId)
    add_sub = Profile.objects.get_or_create()
    return redirect('/')