from django.urls import  path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blogs, name='blogs'),
    path('category_blogs/<str:slug>/', category_blogs, name='category_blogs'),
    path('tag_blogs/<str:slug>/', tag_blogs, name='tag_blogs'),
    path('Mesikel/', Mesikel, name='Mesikel'),
    path('add_blog/', add_blog, name='add_blog'),

]
