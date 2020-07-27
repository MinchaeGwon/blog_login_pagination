from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .form import BlogPost
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects
    cnt = Blog.objects.count()

    #모든 블로그 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 걔를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs': blogs, 'count': cnt, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    blogImg = Blog.objects

    return render(request, 'detail.html', {'blog':blog_detail, 'images': blogImg})

def create(request):
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        form = BlogPost(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPost(instance = blog)
        return render(request, 'new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')
