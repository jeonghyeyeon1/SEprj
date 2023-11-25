from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'



def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # 조건 만족하는 post 레코드 가져옴

    return render(
        request,
        'community/single_post_page.html',
        {
            'post':post,
        }
    )