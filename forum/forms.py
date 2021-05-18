from django import forms
from django.forms import ModelForm, Textarea

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('title', 'content')
        
        widgets={'content': Textarea(attrs={'cols': 20, 'rows': 10})}
