from django.db import models
from django.core.urlresolvers import reverse

# Slugify removes special characters, spaces and anything else
# from strings and adds underscores to make them usable as URLs
from django.utils.text import slugify

# misaka adds links (markdown text) to strings
import misaka

# returns the currect User that is active in the session
from django.contrib.auth import get_user_model

# call things from the current user's session
User = get_user_model()

# To use custom template tags in the features
from django import template
register = template.Library()


class Group(models.Model):

    # The actual name of the group
    name = models.CharField(max_length=256, unique=True)

    # Its slug version, with unicodes included
    slug = models.SlugField(allow_unicode=True, unique=True)

    # a plain text description of the group
    description = models.TextField(blank=True, default='')

    # and one in case you want an HTML description of the group
    description_html = models.TextField(editable=False, default='', blank=True)

    # link all fields to User model from get_user_model(), for all
    # members of the group
    #   > A structural table relationship is created using Groupmember's
    #   > class to add extra arguments
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        # convert the group's name to its slugified form
        self.slug = slugify(self.name)

        # allow HTML in the description using misaka
        self.description_html = misaka.html(self.description)

        # call Model's save() method
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


# class to represent the membership to a group
class GroupMember(models.Model):

    # a FK for the group the user belongs to
    # Related name is 'memberships'
    group = models.ForeignKey(Group, related_name='memberships')

    # and a FK for the currently logged in user, which comes from
    # User = get_user_model()
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    # the meta subclass
    class Meta:
        unique_together = ('group', 'user')
