from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.shortcuts import render
from .models import Post
# Create your views here.


class PostList(ListView):
    model  = Post



class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    pass



class PostDelete(DeleteView):
    pass



class PostUpdate(UpdateView):
    pass