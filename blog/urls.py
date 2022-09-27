# url patterns for the blog app

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'), # localhost:8000/
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/<slug:author>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),

]