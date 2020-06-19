from django.urls import path


from . import views

urlpatterns = [
    path('addProject/',views.add_project,name = "add_project"),
    path("projects/", views.project_index, name="project_index"),
    path("yourprojects/",views.profile_project_index,name="profile_project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("<str:username>/",views.user_project_index,name = "user_project_index"),
path("category/<str:name>/",views.category_project_index,name = "category_project_index"),
]
