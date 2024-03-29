from django import forms
from .models import Post

#Classes

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Title'}),
            'author': forms.Select(attrs={'class': 'form-control','placeholder': 'Enter Author'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder': 'What you thinking ?'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }