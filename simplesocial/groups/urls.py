from django.conf.urls import url
from . import views

app_name = 'groups'

urlpatterns = [

    # show the ListGroups view on groups/
    url(r'^$',
        views.ListGroups.as_view(),
        name='all'),

    # show CreateGroup view on groups/new/
    url(r'^new/',
        views.CreateGroup.as_view(),
        name='create'),

    # show the SingleGroup view of the group name passed as a
    # slugified string on posts/in/<slugified_group_name>
    url(r'posts/in/(?P<slug>[-\w]+)/$',
        views.SingleGroup.as_view(),
        name='single'),

    # on /join/<slugified_group_name>/, call JoinGroup view
    url(r'join/(?P<slug>[-\w]+)/$',
        views.JoinGroup.as_view(),
        name='join'),

    # on /leave/<slugified_group_name>/, call LeaveGroup view
    url(r'leave/(?P<slug>[-\w]+)/$',
        views.LeaveGroup.as_view(),
        name='leave'),
]
