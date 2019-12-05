from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [

    # on posts/ show PostList view for all posts on users and groups
    url(r'^$',
        views.PostList.as_view(),
        name='all'),

    # on posts/new/ show the CreatePost view
    url(r'new/$',
        views.CreatePost.as_view(),
        name='create'),

    # on by/<username> show all posts of a user when you click on
    # him/her (their UserPost view)
    #   > We match them up with the regex (?P<username>[-\w]+)
    url(r'by/(?P<username>[-\w]+)',
        views.UserPosts.as_view(),
        name='for_user'),

    # on by/<username>/<pk> show the PostDetail view of the post
    # written by that username with that PK (a single post)
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',
        views.PostDetail.as_view(),
        name='single'),

    # on delete/<pk> call the DeleteView on the post with that PK
    url(r'delete/(?P<pk>\d+)/$',
        views.DeletePost.as_view(),
        name='delete'),
]
