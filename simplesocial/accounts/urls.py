from django.conf.urls import url

# login and logout WONT be treated inside views.py anymore
# We import views FROM django.contrib.auth module!
# > login and logout functions will come from there
# > we change its name so as not to conflict with the following
#   import statement ('views' recursion)
from django.contrib.auth import views as auth_views

# now import our own views
from . import views

# a name to call our URL templates. Eg: {% url 'accounts:index'%}
app_name = 'accounts'

urlpatterns = [

    # The login view function embedded in django.contrib.auth views
    # > It needs the template to summon itself (template_name)
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),

    # same for logout view.
    # We do not need a template name, since logout redirects to '/'
    url(r'^logout/$',
        auth_views.LogoutView.as_view(),
        name='logout'),

    # Our own views
    url(r'^signup/$',
        views.SignUp.as_view(),
        name='signup')
]
