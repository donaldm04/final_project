from django.conf.urls import url

from .views import index, create_post, remove_post, edit_post, view_post, create_comment, delete_comment, edit_comment

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create_post', create_post, name='create_post'),
    url(r'^remove_post/(?P<post_id>\d+)$', remove_post, name='remove_post'),
    url(r'^edit_post/(?P<post_id>\d+)$', edit_post, name='edit_post'),
    url(r'^view_post/(?P<post_id>\d+)$', view_post, name='view_post'),
    url(r'^create_comment/(?P<post_id>\d+)$', create_comment, name='create_comment'),
    url(r'^delete_comment/(?P<comment_id>\d+)/(?P<post_id>\d+)$', delete_comment, name='delete_comment'),
    url(r'^edit_comment/(?P<comment_id>\d+)/(?P<post_id>\d+)$', edit_comment, name='edit_comment'),
]
