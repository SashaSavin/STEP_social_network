from django.views.generic import ListView, DetailView
from app.models import Post


class ElemsView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post'


class ElemView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
