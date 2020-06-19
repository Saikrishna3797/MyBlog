from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("addpost/", views.add_post,name = "add_post"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<str:projecttitle>/", views.blog_project, name="blog_project"),
]
