"""screened_movie_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import (
    about,write_for_us,tos,privacy,contact,links
)

urlpatterns = [
    path('admin/', admin.site.urls), # localhost:8000/admin
    path('user/', include('user.urls', namespace="user")), # localhost:8000/user
    path('about/',about, name="about"), # localhost:8000/about
    path('write/',write_for_us, name="write_for_us"), # localhost:8000/write
    path('tos/',tos, name="terms_of_service"), # localhost:8000/tos
    path('privacy/',privacy, name="privacy"), # localhost:8000/privacy
    path('contact/',contact, name="contact_us"), # localhost:8000/contact
    path('', include('blog.urls', namespace="blog")), # localhost:8000
    path('summernote/', include('django_summernote.urls')),
    path('links/',links,name="links"),

]

#for serving static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# add a flag for
# handling the 404 error
# handler404 = 'blog.views.error_404_view'

# add a flag for
# handling the 500 error
# handler500 = 'blog.views.error_500_view'