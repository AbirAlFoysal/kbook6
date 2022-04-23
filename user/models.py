from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
from django.urls import reverse, reverse_lazy


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    # post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile', args=(str(self.id)))
    	#return reverse('home')

    def __str__(self):
    	return str(self.user)
