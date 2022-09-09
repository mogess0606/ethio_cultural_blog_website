
from unicodedata import category
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import get_object_or_404,render, redirect
from  django.core.paginator import  PageNotAnInteger, EmptyPage, Paginator


from  .models import  (
    Blog,
    Category,
    Tag
)

from .forms import  AddBlogForm

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
    form = AddBlogForm(request.POST, request.FILES)
    if form.is_valid():
       # user = get_object_or_404(user, pk=request.pk)
        category = get_object_or_404(Category, pk=request.POST["category"])
        blog = form.save(commit=False)
        #blog.user = user
        blog.category = category
        blog.save()
        messages.success(request, "Blog successfully added !")
        return redirect("blog_details", slug=blog.slug)
    else:
        print(form.errors)
    context = {
        "form":form
    }
    return render(request, 'add_blog.html', context)
