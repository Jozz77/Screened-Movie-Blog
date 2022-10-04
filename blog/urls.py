# url patterns for the blog app

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'), # localhost:8000/
    path('post/<slug:author>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.new_post, name='add_post'),
    path('posts/category/<int:category>/', views.category, name='category'),
    path('posts/tag/<slug:tag_slug>/', views.tag, name='tag'),
    path('404/', views.error_404_view, name='error_404'),

]