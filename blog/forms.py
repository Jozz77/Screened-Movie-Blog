from django import forms

from django_summernote.widgets import SummernoteWidget , SummernoteInplaceWidget

from .models import Post

class PostForm(forms.ModelForm):
    
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('cover_image','title','subtitle','slug','content','category','tags','status')
    