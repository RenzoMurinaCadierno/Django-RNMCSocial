# get_user_model() returns the currently active user model
from django.contrib.auth import get_user_model

# and a built-in user creation form is already included in the pack
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:

        # all of this fields come with the UserCreationForm,
        # that will be displayed to the user when signing up
        fields = ('username', 'email', 'password1', 'password2')

        # of anyone entering the website
        model = get_user_model()

    # To set up the labels for those fields, we need to call
    # The __init__ method of this class, summon the super()
    # constructor and add the labels in 'fields' dictionary
    #   > Exactly the same as setting up a label in an HTML form
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'User name'
        self.fields['email'].label = 'Email Address'
