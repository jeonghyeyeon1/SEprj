from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') # 모든 post 레코드 가져와 posts에 저장

    return render(
        request,
        'community/index.html',
        {
            'posts': posts,  # 딕셔너리 형태로 추가
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # 조건 만족하는 post 레코드 가져옴

    return render(
        request,
        'community/single_post_page.html',
        {
            'post':post,
        }
    )