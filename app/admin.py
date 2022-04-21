from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models import Post


class PostAdmin(TranslationAdmin):
    list_display = ('title', 'text',)


admin.site.register(Post, PostAdmin)