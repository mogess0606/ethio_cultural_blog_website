from dataclasses import field, fields
from django import  forms

from .models import Blog


class  AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            "title",
            "category",
            "banner",
            "description"
        )