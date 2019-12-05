from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

# To connect the post with the Group, we need to bring it up
from groups.models import Group

# connect the post to whoever is logged in as a User.
#   > iow, get the current logged in user in the session
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):

    # link the current user as a FK
    user = models.ForeignKey(User, related_name='posts')

    # when the user creates a Post, autocomplete the time
    created_at = models.DateTimeField(auto_now=True)

    message = models.TextField()

    message_html = models.TextField(editable=False)

    # Connect the post to the respective group
    group = models.ForeignKey(
        Group,
        related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):

        # save the post message supporting HTML using misaka
        self.message_html = misaka.html(self.message)

        # call Model's save method
        super().save(*args, **kwargs)

    def get_absolute_url(self):

        # once the message is posted, reverse to the user's posts and
        # to that specific message, which we summon using the PK
        return reverse(
            'posts:single',
            kwargs = {
                'username': self.user.username,
                'pk': self.pk
            }
        )

    class Meta:

        # return the data ordered in desc order (minus)
        ordering = ['-created_at']

        # each message is uniquely linked to the user.
        #   > A user posted message cannot be from another user!
        #   > And two users cannot share a message with the same ID!
        unique_together = ['user', 'message']
