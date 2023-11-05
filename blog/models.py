from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(verbose_name="Title", max_length=200)
	content = models.TextField(verbose_name="Content")
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	date_modified = models.DateTimeField(auto_now=True, blank=True)

	def __str__(self):
		return "%s" % self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, verbose_name="Title", on_delete = models.CASCADE)
	comment = models.TextField(verbose_name="Comment")

	def __str__(self):
		return "%s" % self.comment