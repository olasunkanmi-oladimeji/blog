from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """Model definition for Category."""
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name
    def get_absolute_url(self):
        return reverse('core:category', args=[self.slug])



class Post(models.Model):
    """Model definition for Post."""
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tag')
    title = models.CharField(max_length = 150)
    content = models.TextField()
    video = models.FileField(upload_to='video/',null=True, blank=True)
    image = models.ImageField(upload_to = 'image/',blank=True,null=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def approve_post(self):
        self.publish_date = timezone.now()
        self.save()


    def __str__(self):
        """Unicode representation of Post."""
        return self.title
    def get_absolute_url(self):

        return reverse('core:post', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('Post',related_name="comments",on_delete= models.CASCADE)
    name = models.CharField(max_length =250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        """Unicode representation of Comment."""
        return '%s --- %s' % (self.post.title, self.name)

class Contact(models.Model):
    """Model definition for Contact."""
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.name

