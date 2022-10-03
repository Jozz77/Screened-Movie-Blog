from django import forms

from django_summernote.widgets import SummernoteWidget , SummernoteInplaceWidget

from .models import Post

class TextForm(forms.Form):
    text = forms.CharField(widget=SummernoteWidget(),label='')

    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'summernote', 'placeholder': 'Write here',
        })

class TagForm(forms.Form):
    tags = forms.CharField(widget=forms.Textarea,label='',required=False)
    
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs.update({'placeholder': 'Enter tags separated by commas', 'rows': 1, 'cols': 10})

class PostForm(forms.ModelForm):
    
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('cover_image','title','subtitle','slug','content','category','tags','status')
    