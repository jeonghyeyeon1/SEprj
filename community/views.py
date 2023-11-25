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