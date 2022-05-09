from django.contrib.auth.models import AbstractUser
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    last_online = models.DateTimeField(blank=True, null=True)

    def is_online(self):
        if self.last_online:
            return (timezone.now() - self.last_online) < timezone.timedelta(minutes=1)
        return False

    def get_online_info(self):
        if self.is_online():
            return _('Online')
        if self.last_online:
            return _('Last visit {}').format(naturaltime(self.last_online))
        return _('Unknown')


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default= None, related_name='profile')
    avatar = models.ImageField(upload_to='media/imgs/avatar')
    info = models.CharField(max_length=30)
    subscribers = models.ManyToManyField(User, related_name='subscr', blank=True, default= None)
    is_online = models.BooleanField(default=False)

    def get_friends(self):
        return self.subscribers.all()

    def get_friends_num(self):
        return self.subscribers.all().count()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default=None, null=True, blank=True)

    likes = models.ManyToManyField(User, related_name='post_like')

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Theme(models.Model):
    color = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user

CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=CHOICES)

    def __str__(self):
       return f'{self.sender}-{self.receiver}-{self.status}'


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title