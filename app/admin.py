from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from app.models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(TranslationAdmin):
    form = PostAdminForm
    list_display = ('title', 'text',)


admin.site.register(Post, PostAdmin)