from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

def account_image_url(self, *args, **kwargs):
    return f'account_images/{self.owner}/profile.png'

def default_image_url():
    return f'account_images/account_default.png'

class MyUser(AbstractUser):
    """
    According to the Django documentation, every time we start a project,
    the best thing we can do is create this model (even if the default User 
    meets our needs). In case we want to make changes in the future.
    More info: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """
    pass

class Account(models.Model):
    owner = models.OneToOneField(MyUser, verbose_name='account', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=account_image_url, default=default_image_url, blank=True)
    description = models.CharField(max_length=90, blank=True, 
                                    default="This is my first job at a company as cool as Helpdesk.")
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return f'{self.owner.username} account'.title()

    def social_links(self):
        links = {}
        if self.facebook != '':
            links['facebook'] = self.facebook
        if self.instagram != '':
            links['instagram'] = self.instagram
        if self.twitter != '':
            links['twitter'] = self.twitter

        return links
    

class Rol(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_regular = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

    def get_user_role(self):
        if self.user.rol.is_regular:
            return 'Regular'
        elif self.user.rol.is_agent:
            return 'Agent'
        else:
            return f"You haven't assigned a role"

    def __str__(self):
        if self.user.rol.is_regular:
            return f'{self.user} is regular'.title()
        elif self.user.rol.is_agent:
            return f'{self.user} is agente'.title()
        else:
            return f'{self.user}, unassigned'.title()