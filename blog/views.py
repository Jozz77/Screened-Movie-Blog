from django.shortcuts import render

from .models import Post, Comment , Contact

# Create your views here.

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
    return render(request,"pages/tos.html",context)

# privacy policy page
def privacy(request):
    context = {
        'privacy': "active" 
    }
    return render(request,"pages/privacy.html",context)

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
    return render(request, '404.html')

# error 500 page
def error_500_view(request):
    return render(request, '500.html')

# home page
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
        'home':'active'
    }
    return render(request,"pages/home.html",context)

# post detail page
def post_detail(request, year, month, day, slug, author):
    post = Post.objects.get(slug=slug, author__username=author, publish__year=year, publish__month=month, publish__day=day)
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
def post_new(request):
    context = {
        'post_new':"active"
    }
    return render(request,"pages/write_and_submit.html",context)