from turtle import title
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Post, Comment , Contact

from .forms import PostForm

# Create your views here.

# links to other pages
def links(request):
    context = {
        'links':"active"
    }
    return render(request,"pages/link_to_pages.html",context)

# about page
def about(request):
    context = {
        'about':"active",
        
    }
    return render(request,"pages/about.html",context)

# write for us page
def write_for_us(request):
    context = {
        'write_for_us': "active" 
    }
    return render(request,"pages/write_for_us.html",context)

# terms and conditions page
def tos(request):
    context = {
        'tos': "active"
    }
    return render(request,"pages/terms_of_service.html",context)

# privacy policy page
def privacy(request):
    context = {
        'privacy': "active" 
    }
    return render(request,"pages/privacy_policy.html",context)

# contact us page
def contact(request):
    context = {
        'contact':"active"
    }

    if request.method == 'POST':
        message = request.POST['message']
        if message != None or message != "":
            name = request.POST['name']
            email = request.POST['email']
            # contact = Contact.objects.create(name=name, email=email, message=message)
            # contact.save()
            print(name, email, message)
            context['message'] = "Your message has been sent successfully"
            return render(request,"pages/contact.html",context)

    context['message'] = ""
    return render(request,"pages/contact.html",context)

# error 404 page
def error_404_view(request, exception):
    return render(request, 'pages/404.html')

# error 500 page
def error_500_view(request):
    return render(request, 'pages/500.html')

# home page
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'home':'active'
    }
    return render(request,"pages/home.html",context)

# post detail page
def post_detail(request, author, year, month, day, slug):
    post = Post.objects.get(slug=slug, author__username=author, date_published__year=year, date_published__month=month, date_published__day=day)
    comments = Comment.objects.filter(post=post)
    context = {
        'post':post,
        'comments':comments
    }
    return render(request,"pages/blog_post.html",context)

#  post movie category page
def movies(request):
    context = {
        'movies':"active"
    }
    return render(request,"pages/movies_category.html",context)

# randomgist post page
def random_gist(request):
    context = {
        'random_gist':"active"
    }
    return render(request,"pages/randomGist_category.html",context)

# new post page
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/write_and_submit.html'

    def get_context_data(self,*args, **kwargs):
        context = super(PostCreateView,self).get_context_data(*args,**kwargs)
        context['button'] = "Create"
        return context

    def form_valid(self,form):
        form.instance.author = self.request.user
        if Post.objects.filter(slug=form.instance.slug, title=form.instance.title).exists():
            return render(self.request,"pages/write_and_submit.html",{'error':"Post with this title and slug already exists",
            'button':"Create",
            'form':form
            })
        return super().form_valid(form) 