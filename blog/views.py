from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required



from taggit.models import Tag

from .models import Post, Comment, Contact
from .forms import PostForm, TextForm, TagForm

# Create your views here.

# links to other pages
def links(request):
    context = {"links": "active"}
    return render(request, "pages/link_to_pages.html", context)


# about page
def about(request):
    context = {
        "about": "active",
    }
    return render(request, "pages/about.html", context)


# credits page
def credits(request):
    context = {
        "credits": "active",
    }
    return render(request, "pages/credits.html", context)


# write for us page


def write_for_us(request):
    context = {"write_for_us": "active"}
    return render(request, "pages/write_for_us.html", context)


# terms and conditions page
def tos(request):
    context = {"tos": "active"}
    return render(request, "pages/terms_of_service.html", context)


# privacy policy page
def privacy(request):
    context = {"privacy": "active"}
    return render(request, "pages/privacy_policy.html", context)


# contact us page
def contact(request):
    context = {"contact": "active"}

    if request.method == "POST":
        message = request.POST["message"]
        name = request.POST["name"]
        email = request.POST["email"]
        contact = Contact.objects.create(name=name, email=email, message=message)
        contact.save()
        messages.success(request, "Your form has been sent successfully")
        return HttpResponseRedirect(reverse("contact_us"))

    return render(request, "pages/contact.html", context)


# error 404 page
def error_404_view(request,exception):
    return render(request, "pages/404.html")


def iframe(request):
    return render(request, "pages/iframe.html")


# error 500 page
def error_500_view(request):
    return render(request, "pages/500.html")


# home page
def home(request):
    posts = Post.published.all()
    movies = posts.exclude(category=5)[0:4]
    tv_series = posts.filter(category=5)[0:4]
    latest_posts = posts.order_by("-date_published")[0:10]

    context = {
        "posts": posts,
        "home": "active",
        "movies": movies,
        "tv_series": tv_series,
        "latest_posts": latest_posts,
    }

    return render(request, "pages/home.html", context)


# post detail page
def post_detail(request, author, year, month, day, slug):
    post = Post.objects.get(
        slug=slug,
        author__username=author,
        date_published__year=year,
        date_published__month=month,
        date_published__day=day,
    )
    next_post = (
        Post.objects.filter(date_published__gt=post.date_published)
        .order_by("date_published")
        .first()
    )
    comments = Comment.objects.filter(post=post)
    post_tag_ids = post.tags.values_list("id", flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-date_published"
    )[:5]
    related_post = similar_posts[0:1]
    similar_posts = similar_posts[1:5]
    latest_posts = Post.published.all().order_by("-date_published")[0:10]

    context = {
        "post": post,
        "comments": comments,
        "similar_posts": similar_posts,
        "related_post": related_post,
        "next_post": next_post,
        "latest_posts": latest_posts,
    }
    return render(request, "pages/blog_post.html", context)


def get_title_and_subtitle(req_type, category):
    if req_type == "category":
        if category == 1:
            title = "Hollywood"
            subtitle = "<p>This category covers everything related to movies written here on Screened. Our category is quite large and diverse, since movies cover a major portion of the site’s content. We have several smaller subcategories within it, as well as several categories that are a combination of one or more categories. Whether you’re here for the latest news and release dates, analyses, suggestions, or simply some information about a movie or two, we have it all.</p><br><p>From black and white silent classics to modern blockbusters, the writers of our movie section cover it all. Our writers have made movies their life and that passion is clearly reflected in the articles they are writing, which range from basic information-based text, via various lists, to complex narrative and psychological analyses of the movies and the characters.</p><br><p>Our Movies section is not just one of our largest, it is one of our most diverse categories and we hope you’ll find everything you’re looking for there.</p>"

        elif category == 2:
            title = "Bollywood"
            subtitle = "Bollywood is the largest film industry in India, producing over 200 movies a year. It is also the largest film industry in the world in terms of the number of people employed. The industry is based in Mumbai, Maharashtra, and is a part of the larger cinema of India, which includes other production centers producing films in various other Indian languages. The name Bollywood is a portmanteau of Bombay (the former name for Mumbai) and Hollywood, the center of the American film industry. Bollywood is also one of the largest centers of film production in the world. The name Bollywood is a portmanteau of Bombay (the former name for Mumbai) and Hollywood, the center of the American film industry. Bollywood is also one of the largest centers of film production in the world."

        elif category == 3:
            title = "Nollywood"
            subtitle = "Nollywood is the informal name given to the Nigerian film industry, based in the Nigerian city of Lagos.\nThe Nigerian film industry is the second largest in the world in terms of the number of films produced annually, and the third largest in terms of the number of people employed.\nThe Nigerian film industry is the second largest in the world in terms of the number of films produced annually, and the third largest in terms of the number of people employed."

        elif category == 4:
            title = "K-Drama"
            subtitle = "Everything Korean drama."

        elif category == 5:
            title = "TV Series"
            subtitle = "Everything TV Series."
        else:
            title = "No such category"
            subtitle = "Category does not exist"

    elif req_type == "tag":
        title = ""
        subtitle = ""

    else:
        title = "Search Results"
        subtitle = "Search Results"
    return title, subtitle


#  post movie category page
def category(request, category):
    posts = Post.published.all().filter(category=category)
    latest_posts = Post.published.all().order_by("-date_published")[0:10]
    paginator = Paginator(posts, 8)
    page = request.GET.get("page")
    title, subtitle = get_title_and_subtitle("category", category)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "movies": "active",
        "posts": posts,
        "title": title,
        "subtitle": subtitle,
        "page": page,
        "latest_posts": latest_posts,
    }
    return render(request, "pages/category.html", context)


def comment(request, post_id):

    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        name = request.POST.get("username")
        message = request.POST.get("comment-message")
        comment = Comment(name=name, body=message, post=post)
        comment.save()
        return redirect(post.get_absolute_url() + "#comments")


def latest_posts(request):
    posts = Post.published.all().order_by("-date_published")
    latest_posts = Post.published.all().order_by("-date_published")[0:10]
    paginator = Paginator(posts, 8)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "posts": posts,
        "latest_posts": latest_posts,
        "page": page,
        "title": "Latest Posts",
        "subtitle": "Latest Posts",
    }
    return render(request, "pages/category.html", context)


def search(request):
    query = None
    results = []
    latest_posts = Post.published.all().order_by("-date_published")[0:10]
    if request.method == "POST":
        query = request.POST.get("query")
        results = Post.published.annotate(
            search=SearchVector("title", "content"),
        ).filter(search=query)
        paginator = Paginator(results, 8)
        page = request.GET.get("page")
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

    context = {
        "query": query,
        "latest_posts": latest_posts,
        "title": "Search Results for: " + query,
        "posts": results,
    }
    return render(request, "pages/category.html", context)


def tag(request, tag_slug):
    tag_slug = slugify(tag_slug)
    latest_posts = Post.published.all().order_by("-date_published")[0:10]
    related_posts = Post.published.all()
    tag = get_object_or_404(Tag, slug=tag_slug)
    related_posts = related_posts.filter(tags__in=[tag])
    paginator = Paginator(related_posts, 8)
    page = request.GET.get("page")

    try:
        related_posts = paginator.page(page)
    except PageNotAnInteger:
        related_posts = paginator.page(1)
    except EmptyPage:
        related_posts = paginator.page(paginator.num_pages)
    context = {
        "posts": related_posts,
        "tag": tag,
        "tag_slug": tag_slug,
        "latest_posts": latest_posts,
    }
    return render(request, "pages/category.html", context)


@login_required
def new_post(request):
    if request.method == "POST":
        form = request.POST
        content_form = TextForm()
        tag_form = TagForm()
        title = form["title"]
        subtitle = form["subtitle"]
        slug = slugify(form["slug"])
        author = request.user
        category = int(form["category"])
        status = int(form["status"])
        content = form["text"]
        tags = form["tags"].split(",")

        try:
            cover_image = request.FILES["cover_image"]
        except Exception:
            cover_image = None

        if Post.objects.filter(slug=slug, title=title).exists():
            return render(
                request,
                "pages/write_and_submit.html",
                {
                    "error": "Post with this title and slug already exists",
                    "button": "Create",
                    "form": content_form,
                    "tag_form": tag_form,
                },
            )
        post = Post.objects.create(
            title=title,
            subtitle=subtitle,
            cover_image=cover_image,
            slug=slug,
            author=author,
            category=category,
            status=status,
            content=content,
        )
        for tag in tags:
            post.tags.add(tag)
        post.save()
        messages.success(request, "Post created successfully")
        return redirect(post.get_absolute_url())

        
            

    else:
        content_form = TextForm()
        tag_form = TagForm()
    return render(
        request,
        "pages/write_and_submit.html",
        {"form": content_form, "tag_form": tag_form},
    )


def edit_post(request, author, year, month, day, slug):

    if request.user.username != author:
        return HttpResponseForbidden()

    post = Post.objects.get(
        slug=slug,
        author__username=author,
        date_published__year=year,
        date_published__month=month,
        date_published__day=day,
    )
    if post.status == 0:
        _draft = "selected"
        _published = ""
    else:
        _draft = ""
        _published = "selected"

    if post.category == 1:
        _hollywood = "selected"
        _bollywood = ""
        _nollywood = ""
        _kdrama = ""
        _tvseries = ""
    elif post.category == 2:
        _bollywood = "selected"
        _hollywood = ""
        _nollywood = ""
        _kdrama = ""
        _tvseries = ""

    elif post.category == 3:
        _nollywood = "selected"
        _hollywood = ""
        _bollywood = ""
        _kdrama = ""
        _tvseries = ""

    elif post.category == 4:
        _kdrama = "selected"
        _hollywood = ""
        _bollywood = ""
        _nollywood = ""
        _tvseries = ""

    elif post.category == 5:
        _tvseries = "selected"
        _hollywood = ""
        _bollywood = ""
        _nollywood = ""
        _kdrama = ""

    if request.method == "POST":
        form = request.POST
        content_form = TextForm()
        tag_form = TagForm()
        title = form["title"]
        subtitle = form["subtitle"]
        slug = slugify(form["slug"])
        youtube_link = form["trailer"]
        author = request.user
        category = int(form["category"])
        status = int(form["status"])
        content = form["text"]
        tags = form["tags"].split(",")



        if Post.objects.filter(slug=slug, title=title).exists() and post.slug != slug:
            return render(
                request,
                "pages/write_and_submit.html",
                {
                    "error": "Post with this title and slug already exists",
                    "button": "Create",
                    "form": content_form,
                    "tag_form": tag_form,
                },
            )

        post.title = title
        post.subtitle = subtitle
        post.slug = slug
        post.category = category
        post.status = status
        post.content = content
        post.youtube_url = youtube_link
        post.tags.clear()

        for tag in tags:
            post.tags.add(tag)

        messages.success(request, "Post updated successfully")
        post.save()

        return redirect(post.get_absolute_url())

    else:
        content_form = TextForm(initial={"text": post.content})
        _tags = []
        for tag in post.tags.all():
            _tags.append(tag.name)
        tag_form = TagForm(initial={"tags": ",".join(_tags)})

    return render(
        request,
        "pages/write_and_submit.html",
        {
            "form": content_form,
            "tag_form": tag_form,
            "post": post,
            "draft": _draft,
            "published": _published,
            "hollywood": _hollywood,
            "bollywood": _bollywood,
            "nollywood": _nollywood,
            "kdrama": _kdrama,
            "tvseries": _tvseries,
        },
    )


def delete_post(request, author, year, month, day, slug):
    if request.user.username != author:
        return HttpResponseForbidden()

    post = Post.objects.get(
        slug=slug,
        author__username=author,
        date_published__year=year,
        date_published__month=month,
        date_published__day=day,
    )
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect("blog:home")
