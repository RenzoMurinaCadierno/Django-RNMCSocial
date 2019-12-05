from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views import generic
from django.http import Http404

from braces.views import SelectRelatedMixin

from . import models, forms

# When a user is logged in, we can grab it as an object and
# work with it
from django.contrib.auth import get_user_model
User = get_user_model()


# List view class for the Post objects as a whole
class PostList(SelectRelatedMixin, generic.ListView):

    # link up the Post model with the List view
    model = models.Post

    # A tuple for the foreign keys of this post's owners
    #   > The user this post belongs to, and the group this post
    #     belongs to
    select_related = ('user', 'group')


# List view class for the Post objects that belongs to a user
class UserPosts(generic.ListView):

    model = models.Post

    template_name = 'posts/user_post_list.html' #posts/user_post_list

    def get_queryset(self):

        # try assigning this objects post_user to the posts of the
        # User object (logged in at the time), with the exact same
        # username as the current User.
        #   > In other words, fetch all posts of that user
        #   > and the posts will be stored in post_user_posts
        try:            # self.post.user?
            self.post_user = \
                User.objects\
                    .prefetch_related('posts')\
                    .get(username__iexact=self.kwargs.get('username'))

        # if the to prefetch the posts does not exist, 404
        except User.DoesNotExist:
            raise Http404

        # if you could fetch the posts from the current logged in
        # user, return them
        else:
            return self.post_user.posts.all()

    # get the context dictionary (data) to pass
    def get_context_data(self, **kwargs):

        # bring up ListView's context data first
        context = super().get_context_data(**kwargs)

        # add the value in 'post_user' key
        context['post_user'] = self.post_user

        # return the context dictionary
        return context


# Detail view class for the Post objects as a whole
class PostDetail(SelectRelatedMixin, generic.DetailView):

    model = models.Post

    select_related = ('user', 'group')

    def get_queryset(self):

        # get the queryset for the Posts' DetailView (all posts)
        queryset = super().get_queryset()

        # filter them by the ones the current logged in user typed
        return queryset.filter(
            user__username__iexact=self.kwargs.get('username'))


# Create view class for the Post objects as a whole
class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):

    fields = ('message', 'group')

    model = models.Post

    def form_valid(self, form):

        # link the CreatePost object object attrib to this saved form
        # do not commit until we check that the user is valid
        self.object = form.save(commit=False)

        # request and validate the user. Save it in user attrib
        self.object.user = self.request.user

        # now save the form
        self.object.save()

        # call for form_valid method of CreateView, pass this modified
        # form, which will save it.
        return super().form_valid(form)


# Delete view class for the Post objects as a whole
class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):

    model = models.Post

    select_related = ('user', 'group')

    success_url = reverse_lazy('posts:all')

    def get_queryset(self):

        queryset = super().get_queryset()

        # filter the posts by the ones created by the current user's id
        return queryset.filter(user_id = self.request.user.id)

    # standard delete method for DeleteView
    def delete(self, *args, **kwargs):

        # show a success message with the deleted post
        messages.success(self.request, 'Post Deleted')

        # delete the message using delete() from DeleteView
        return super().delete(*args, **kwargs)
