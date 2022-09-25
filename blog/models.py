from django.db import models
from django.utils import timezone
from django.urls import reverse

from user.models import CustomUser

from taggit.managers import TaggableManager

CATEGORY = ((1 , 'Movies'), (2, 'Tv shows'))
STATUS = ((0, 'Draft'), (1, 'Published'))

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=1)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    category = models.IntegerField(choices=CATEGORY)
    tags = TaggableManager()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager() # The default manager.
    published = PublishedManager()

    class Meta:
        ordering = ('-date_published',)

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[
            self.date_published.year,
            self.date_published.month,
            self.date_published.day,
            self.slug,
            self.author.username,
        ])

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)