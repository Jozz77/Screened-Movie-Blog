from django.shortcuts import render,get_object_or_404

from .models import CustomUser
from blog.models import Post

# Create your views here.

#login page
def login(request):
    return render(request, 'accounts/login.html')

#password request code , form to fill
def password_reset(request):
    return render(request, 'accounts/request_code.html')

#response after filling the form
def password_reset_confirm(request):
    return render(request, 'accounts/reset_link.html')

#password reset form , changing the password
def password_reset_complete(request):
    return render(request, 'accounts/password_reset.html')

# registering new users
def signup(request):
    return render(request, 'accounts/signup.html')

#user profile
def profile(request, author):
    author = get_object_or_404(CustomUser, username=author)
    articles = Post.objects.filter(author=author).order_by('-date_created') 
    latest_posts = Post.published.all().order_by('-date_published')[0:10]
    print(latest_posts)

    context = {
        'author':author,
        'articles':articles,
        'latest_posts':latest_posts,
    }
    return render(request, 'pages/author_profile.html', context)

