from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def post_list(request):
    # return HttpResponse("hello list")
    # posts = [
    #     {"id": 1, "title": "第一篇文章"},
    #     {"id": 2, "title": "蒸蚌！"},
    # ]
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts":posts})

def post_detail(request, pk: int):
    # return HttpResponse(f"hello detail: {pk}")
    # post = {
    #     "id": pk,
    #     "title": f"第{pk}篇文章",
    #     "content": "这是文章内容，之后会从数据库读取。"
    # }
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post":post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:post_detail", pk=post.pk)

    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("你没有权限编辑这篇文章")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {"form": form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if post.author != request.user:
        return HttpResponseForbidden("你没有权限删除这篇文章")

    if request.method == "POST":
        post.delete()
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {"post":post})