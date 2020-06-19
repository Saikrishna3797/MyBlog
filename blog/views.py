from django.shortcuts import render,redirect

from blog.forms import CommentForm,newPostForm
from blog.models import Post, Comment
from projects.models import Project


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "blog_index.html", context)


def blog_project(request, projecttitle):
    project = Project.objects.get(title=projecttitle)
    posts = Post.objects.filter(project=project).order_by(
        "-created_on"
    )
    context = {"project": project, "posts": posts}
    return render(request, "blog_project.html", context)

def add_post(request):
    if request.method == "POST":
        form = newPostForm(request.POST)
        if form.is_valid():
            post_x = Post(
                user = request.user,
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                project = form.cleaned_data['project'],)
            post_x.save()
            return redirect('blog_index')
    else:
        form = newPostForm()
    return render(request, 'add_post.html', {'form': form})

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                user = request.user,
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            form = CommentForm()
            redirect('add_post')

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog_detail.html", context)
