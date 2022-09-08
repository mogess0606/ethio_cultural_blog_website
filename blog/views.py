
from multiprocessing import context
from django.shortcuts import render, redirect
from  django.core.paginator import  PageNotAnInteger, EmptyPage, Paginator

from  .models import  (
    Blog,
    Tag
)

# Create your views here.

def home(request):
    blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-create_date')
    context = {
        "blogs": blogs,
        "tags": tags
        
    }
    return render(request, 'home.html', context)


def blogs(request):
    queryset = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-create_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
         blogs = paginator.page(1)
       
        
    
    context = {
        "blogs": blogs,
        "tags": tags,
        "paginator": paginator
        
    }
    return render(request, 'blogs.html', context)




def category_blogs(request, slug):
    category = get_object_or_404(category, slug=slug)
    queryset = category.Category_blogs.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    all_blogs = Blog.objects.order_by('-created_date')[:5]
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
         blogs = paginator.page(1)
    context = {
        "blogs": blogs,
        "tags": tags   
    }
    return render(request, 'category_blogs.html', context)



def tag_blogs(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    queryset = tag.tag_blogs.all()
    tags = Tag.objects.order_by('-created_date')[:5]
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    all_blogs = Blog.objects.order_by('-created_date')[:5]
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
         blogs = paginator.page(1)
    context = {
        "blogs": blogs,
        "tags": tags   
    }
    return render(request, 'tag_blogs.html', context)

def Mesikel(request):
    return render(request, 'Mesikel.html')


def add_blog(request):
    return render(request, 'add_blog.html')
