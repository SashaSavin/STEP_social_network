
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns

from chat.views import channel, room

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('app.urls')),
    path('chat/', channel),
    path('chat/<str:room_name>/', room, name='room'),
)
