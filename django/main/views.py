from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    postAll = Post.objects.all()# 전체 게시물 넘겨주기
    # return render(request, 'main/index.html')
    return render(request, 'main/index.html', {'postAll':postAll})
