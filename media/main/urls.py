from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    path('signup',views.signup_view,name="signup"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('settings',views.settings,name="settings"),
    path('like_post',views.like_post,name="like_post"),
    path('profile/<int:pk>',views.profile_views,name="profile"),
]