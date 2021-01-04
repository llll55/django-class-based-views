from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.shortcuts import render
from .models import Post
# Create your views here.


class PostList(ListView):
    model = Post     ##  in template [ object_list , post_list  ]
    ordering = ['created_at']
    #queryset = Post.objects.filter(active=True)

    def get_queryset(self):
        return Post.objects.filter(active=True)

class PostDetail(DetailView):
    pass



class PostCreate(CreateView):
    pass



class PostDelete(DeleteView):
    pass



class PostUpdate(UpdateView):
    pass