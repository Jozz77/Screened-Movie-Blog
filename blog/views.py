from django.shortcuts import render

from .models import Post, Comment , Contact

# Create your views here.
def about(request):
    context = {
        'about':"active",
        
    }
    return render(request,"pages/about.html",context)

def write_for_us(request):
    context = {
        'write_for_us': "active" 
    }
    return render(request,"pages/write_for_us.html",context)

def tos(request):
    context = {
        'tos': "active"
    }
    return render(request,"pages/tos.html",context)

def privacy(request):
    context = {
        'privacy': "active" 
    }
    return render(request,"pages/privacy.html",context)

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

def error_404_view(request, exception):
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'home':'active'
    }
    return render(request,"pages/home.html",context)

def post_detail(request, year, month, day, slug, author):
    post = Post.objects.get(slug=slug, author__username=author, publish__year=year, publish__month=month, publish__day=day)
    comments = Comment.objects.filter(post=post)
    context = {
        'post':post,
        'comments':comments
    }
    return render(request,"pages/blog_post.html",context)

def movies(request):
    context = {
        'movies':"active"
    }
    return render(request,"pages/movies_category.html",context)

def random_gist(request):
    context = {
        'random_gist':"active"
    }
    return render(request,"pages/randomGist_category.html",context)

def post_new(request):
    context = {
        'post_new':"active"
    }
    return render(request,"pages/write_and_submit.html",context)