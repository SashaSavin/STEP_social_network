from django.views.generic import ListView, DetailView
from app.models import Post
from .mixins import AdminAuthMixin


class ElemsView(ListView):
    model = Post
    template_name = 'chat.html'
    context_object_name = 'post'


class ElemView(AdminAuthMixin, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
