from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from . forms import CommentForm
from django.views.generic.edit import CreateView


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'author', 'academic_year', 'body', ]
