from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
	template = "list.html"
	posts = Post.objects.only('title', 'content', 'date_posted')
	context = {
		'posts':posts,
	}
	return render(request, template, context)

def create_post(request):
	template = "create_post.html"
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'post_form': PostForm(),
		}
		return render(request, template, context)

def edit_post(request, post_id):
	template = "edit_post.html"
	post = Post.objects.get(id=int(post_id))

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'post_form': PostForm(instance=post),
		}
		return render(request, template, context)

def remove_post(request, post_id):
	post = Post.objects.get(id=int(post_id))
	post.delete()
	return HttpResponseRedirect(reverse_lazy('blog:index'))

def view_post(request, post_id):
	template = "view_post.html"
	post = Post.objects.get(id=int(post_id))
	comments = Comment.objects.filter(post_id=int(post_id))
	context = {
		'post':post,
		'comments':comments,
	}
	return render(request, template, context)

def create_comment(request, post_id):
	template = "create_comment.html"
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			form.instance.post_id = post_id
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:view_post', kwargs={'post_id': post_id}))
	else:
		context = {
			'comment_form': CommentForm(),
		}
		return render(request, template, context)

def delete_comment(request, comment_id, post_id):
	comment = Comment.objects.get(id=int(comment_id))
	comment.delete()
	return HttpResponseRedirect(reverse_lazy('blog:view_post', kwargs={'post_id': post_id}))

def edit_comment(request, comment_id, post_id):
	template = "edit_comment.html"
	comment = Comment.objects.get(id=int(comment_id))

	if request.method == "POST":
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:view_post', kwargs={'post_id': post_id}))
	else:
		context = {
			'comment_form': CommentForm(instance=comment),
		}
		return render(request, template, context)