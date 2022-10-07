from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'user'

urlpatterns = [
        path('login/',views.signin,name='login'),
        path('password_reset/',views.password_reset,name='password_reset'),
        path('password_reset_confirm/',views.password_reset_confirm,name='password_reset_confirm'),
        path('password_reset_complete/',views.password_reset_complete,name='password_reset_complete'),
        path('signup/',views.signup,name='signup'),
        path('logout/',auth_views.LogoutView.as_view(),name='logout'),
        path('profile/<slug:author>/',views.profile,name='profile'),
        
]