from django.shortcuts import render, redirect, get_object_or_404,  HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        if request.method == 'POST': 
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            username = request.POST['username']

            if CustomUser.objects.get(email=email, username=username):
                print('User not')
                return HttpResponseRedirect('/')

            else:
                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
                user.save()
                print('User created')
                return redirect('user:login')
                

        else:
            return render(request, 'accounts/signup.html')

#user profile
def profile(request, author):
    author = get_object_or_404(CustomUser, username=author)
    articles = Post.objects.filter(author=author).order_by('-date_created') 
    latest_posts = Post.published.all().order_by('-date_published')[0:10]
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
        
    context = {
        'author':author,
        'articles':articles,
        'latest_posts':latest_posts,
    }
    return render(request, 'pages/author_profile.html', context)


