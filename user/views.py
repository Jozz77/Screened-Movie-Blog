from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import authenticate, login
from blog.models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.

#login page
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = get_object_or_404(CustomUser, email=email).username

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('blog:home')
        else: 
            messages.error(request, 'Invalid credentials')
            return redirect('user:login')
    else:
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

            if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect('user:signup')

            
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
            user.save()
            messages.success(request, 'You have successfully registered')
            return redirect('user:login')
                
        else:
            return render(request, 'accounts/signup.html')

#user profile

def profile(request, author):
    author = get_object_or_404(CustomUser, username=author)
    articles = Post.objects.filter(author=author).order_by('-date_created') 
    latest_posts = Post.published.all().order_by('-date_published')[0:10]
    context = {
        'author':author,
        'posts':articles,
        'latest_posts':latest_posts,
    }
    return render(request, 'pages/author_profile.html', context)

@login_required
def edit_profile(request, author):

    if request.user.username != author:
        messages.error(request, 'You are not allowed to edit this profile')
        return redirect('blog:home')

    if request.method == 'POST':
        author = get_object_or_404(CustomUser, username=author)
        author.first_name = request.POST['first-name']
        author.last_name = request.POST['last-name']
        author.bio = request.POST['bio']
        author.twitter_link = request.POST['twitter-link']
        author.instagram_link = request.POST['ig-link']
        author.pinterest_link = request.POST['pinterest-link']
        author.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('user:profile', author=author)
    else:
        return redirect('user:profile', author=author)
