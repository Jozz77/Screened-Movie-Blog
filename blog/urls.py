# url patterns for the blog app

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'), # localhost:8000/
    path('post/<slug:author>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:author>/<int:year>/<int:month>/<int:day>/<slug:slug>/edit', views.edit_post, name='edit_post'),
    path('post/<slug:author>/<int:year>/<int:month>/<int:day>/<slug:slug>/delete', views.delete_post, name='delete_post'),
    path('post/new/', views.new_post, name='add_post'),
    path('posts/tag/<slug:tag_slug>/', views.tag, name='tag'),
    path('posts/category/<int:category>/', views.category, name='category'),
    path('latest/', views.latest_posts, name='latest'),
    path('search/', views.search, name='search'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('404/', views.error_404_view, name='error_404'),

]