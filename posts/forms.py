from django import forms
from .models import Post

class BoardPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'published_date')
        
        # author also needs to be included above, when implemented