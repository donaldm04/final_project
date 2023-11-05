from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		#fields = "__all__"
		fields = ('title', 'content')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control'}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		#fields = "__all__"
		fields = ('comment',)
		labels = {
			'comment':'',
		}

		widgets = {
			'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write a comment...'}),
		}
