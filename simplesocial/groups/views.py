from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)

# bring your models up
from groups.models import Group, GroupMember

# Bring the models from these groups
from . import models


# CreateView = Create + model name (Group)
class CreateGroup(LoginRequiredMixin, generic.CreateView):

    # only bring the fields name and description for the user to
    # specify when creating a group
    fields = ('name', 'description')

    # connect to the model Group
    model = Group


# A detail view for the Group
class SingleGroup(generic.DetailView):

    model = Group


# and a list view for them
class ListGroups(generic.ListView):

    model = Group


# Add a view for when sb joins a group.
#   > RedirectView is to redirect the user to a page when
#     get_redirect_url is called
class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        """ Reverse the user to groups:single url, pass the slug
        of the joined group to connect to it. """

        return reverse(
            'groups:single',
            kwargs={'slug': self.kwargs.get('slug')}
        )

    def get(self, request, *args, **kwargs):
        """ Retrieves the group, tries to join the user into it and
        display a message on success or error. Finally, call the
        parent's get() method. """

        # try to get the group to join or raise 404 otherwise
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        # try creating a group member for the group you want to join,
        # passing the user that is requesting to join and the group
        # to join as args
        try:
            GroupMember.objects.create(user=self.request.user, group=group)

        # The user is already inside the group, which raises an
        # IntegrityError (due to key duplication). Show the user a
        # message telling them that.
        except IntegrityError:
            messages.warning(self.request, 'You are already a member!')

        # The GroupMember object could be created, greet the user.
        else:
            messages.success(self.request, 'You are now a member of the group!')

        # finally, call the parent's get() method
        return super().get(request, *args, **kwargs)


# And one class for when they leave
class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        return reverse(
            'groups:single',
            kwargs={'slug': self.kwargs.get('slug')}
        )

    def get(self, request, *args, **kwargs):

        # filter all GroupMember objects until you find one that
        # matches the requesting user trying to leave it, and the
        # corresponding slug name of the group
        try:
            membership = models.GroupMember.objects.filter(
                user = self.request.user,
                group__slug = self.kwargs.get('slug')
            )

        # The requesting user is not a member of the group.
        except models.GroupMember.DoesNotExist:

            messages.warning(
                self.request, 'You are not a member of this group.')

        # Once the group was found and it is certain that the user
        # belongs to it, remove the user from the group.
        else:

            membership.delete()
            messages.success(self.request, 'You have left the group.')

        # Lastly, call the base class's get() method
        return super().get(request, *args, **kwargs)
