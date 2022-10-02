from django.shortcuts import render, get_object_or_404 , HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from taggit.models import Tag

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
        name = request.POST['name']
        email = request.POST['email']
        contact = Contact.objects.create(name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Your form has been sent successfully')
        return HttpResponseRedirect(reverse('contact_us'))

    return render(request,"pages/contact.html",context)

# error 404 page
def error_404_view(request):
    return render(request, 'pages/404.html')

# error 500 page
def error_500_view(request):
    return render(request, 'pages/500.html')

# home page
def home(request):
    posts = Post.published.all()
    movies = Post.published.all().exclude(category=5)[0:4]
    tv_series = Post.published.all().filter(category=5)[0:4]

    category_tv_series = Post.published.all().filter(category=5)[0:1]
    category_hollywood = Post.published.all().filter(category=1)[0:1]
    category_bollywood = Post.published.all().filter(category=2)[0:1]
    category_nollywood = Post.published.all().filter(category=3)[0:1]
    category_k_drama = Post.published.all().filter(category=4)[0:1]

    latest_post = Post.published.all()[0:1]
    lastest_posts = Post.published.all()[1:10]

    context = {
        'posts':posts,
        'home':'active',
        'movies': movies,
        'tv_series':tv_series,
        'category_tv_series':category_tv_series,
        'category_hollywood':category_hollywood,
        'category_bollywood':category_bollywood,
        'category_nollywood':category_nollywood,
        'category_k_drama':category_k_drama,
        'latest_post':latest_post,
        'lastest_posts':lastest_posts
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
def category(request, category):
    posts = Post.published.all().filter(category=category)

    if category == 1:
        category_title = "Hollywood"
        category_subtitle = "This category covers everything related to hollywood written here on Screened. Our category is quite large and diverse, since movies cover a major portion of the site’s content. We have several smaller subcategories within it, as well as several categories that are a combination of one or more categories. Whether you’re here for the latest news and release dates, analyses, suggestions, or simply some information about a movie or two, we have it all.\nFrom black and white silent classics to modern blockbusters, the writers of our movie section cover it all. Our writers have made movies their life and that passion is clearly reflected in the articles they are writing, which range from basic information-based text, via various lists, to complex narrative and psychological analyses of the movies and the characters.\nOur Movies section is not just one of our largest, it is one of our most diverse categories and we hope you’ll find everything you’re looking for there."

    elif category == 2:
        category_title = "Bollywood"
        category_subtitle = "Bollywood is the largest film industry in India, producing over 200 movies a year. It is also the largest film industry in the world in terms of the number of people employed. The industry is based in Mumbai, Maharashtra, and is a part of the larger cinema of India, which includes other production centers producing films in various other Indian languages. The name Bollywood is a portmanteau of Bombay (the former name for Mumbai) and Hollywood, the center of the American film industry. Bollywood is also one of the largest centers of film production in the world. The name Bollywood is a portmanteau of Bombay (the former name for Mumbai) and Hollywood, the center of the American film industry. Bollywood is also one of the largest centers of film production in the world."

    elif category == 3:
        category_title = "Nollywood"
        category_subtitle = "Nollywood is the informal name given to the Nigerian film industry, based in the Nigerian city of Lagos.\nThe Nigerian film industry is the second largest in the world in terms of the number of films produced annually, and the third largest in terms of the number of people employed.\nThe Nigerian film industry is the second largest in the world in terms of the number of films produced annually, and the third largest in terms of the number of people employed."

    elif category == 4:
        category_title = "K-Drama"
        category_subtitle = "Everything Korean drama."

    elif category == 5:
        category_title = "TV Series"
        category_subtitle = "Everything TV Series."

    else:
        category_title = "No such category"
        category_subtitle = "Category does not exist"

    context = {
        'movies':"active",
        'posts':posts,
        'category_title':category_title,
        'category_subtitle':category_subtitle
    }
    return render(request,"pages/category.html",context)

def tag(request, tag_slug):
    related_posts = Post.published.all()
    tag = get_object_or_404(Tag, slug=tag_slug)
    related_posts = related_posts.filter(tags__in=[tag])[0:20]
    print(related_posts)
    context = {
        'posts':related_posts,
        'tag':tag
    }
    return render(request,"pages/category.html",context)

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