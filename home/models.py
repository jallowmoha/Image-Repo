from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.


def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)


class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default="")
    date_created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date_created"]

    def __str__(self):
        return self.title
