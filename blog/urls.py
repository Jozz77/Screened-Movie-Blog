# url patterns for the blog app

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'), # localhost:8000/
    path('post/<slug:author>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='add_post'),

]