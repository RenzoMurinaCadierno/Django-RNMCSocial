from django.contrib import admin
from . import models


# Add a tabular class to allow edits on single groups in the
# admin page whenever you hop into the registered global Group model
class GroupMemberInline(admin.TabularInline):

    # link the model to GroupMembers, which is already linked
    # up with Groups
    model = models.GroupMember


#  now register the Group model (parent class)
admin.site.register(models.Group)
