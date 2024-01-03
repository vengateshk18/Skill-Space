from django.urls import path
from . import views
from . import resume
urlpatterns=[
    path('home',views.home,name="home"),
    path('',views.home,name="home"),
    path('signup',views.signup_view,name="signup"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('settings',views.settings,name="settings"),
    path('like_post',views.like_post,name="like_post"),
    path('profile/<pk>',views.profile_views,name="profile"),
    path('delete_post/<str:id>',views.delete_post,name="delete_post"),
    path('follower',views.check_follower,name="follower"),
    path('resume',views.resume,name="resume"),
    path('username_suggestions/', views.username_suggestions, name='username_suggestions'),
    path('professionalprof',resume.professionalprof,name="professinalprof"),
    path('projects',resume.projects,name="projects"),
    path('internship',resume.internship,name="internship"),
    path('favpost/<uuid:post>',views.favpost_add,name="favpost_add"),
    path('favpost',views.favpost,name="favpost"),
    path('delete_favpost/<int:pk>',views.delete_fav,name="delete_favpost"),
    path('profile_analytics',resume.profile_analytics,name="profile_analytics"),
    path('show/education',resume.showEducation,name="showeducation"),
]