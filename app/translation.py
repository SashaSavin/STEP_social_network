from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from app.models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', )
    required_languages = ('ru', 'en')