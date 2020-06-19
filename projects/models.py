from django.db import models
from django.contrib.auth.models import User

class ProjectCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField()
    projectcategory = models.ForeignKey("ProjectCategory",on_delete=models.CASCADE)
    #image = models.FilePathField(path="projects/static/img/")

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title+' -   by : '+self.user.username