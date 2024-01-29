from django.urls import path
from . import views

urlpatterns=[
    path('show-quiz',views.quizmain,name="show-quiz"),
]