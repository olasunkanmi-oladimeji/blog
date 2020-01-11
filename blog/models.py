from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
# Create your models here.
class blogpost(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text=models.TextField()
    images=models.ImageField(upload_to="pic",blank=True, null=True)
    created_date=models.DateField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    def publish(self):
        self.publish_date=datetime.datetime()
        self.save()
    def get_absolute_url(self): 
        return reverse('postdetail', kwargs={'pk': self.pk})
    def comment_approved(self):
        return self.comment.filter(approved_comment=True)

class commentpost(models.Model):
    post=models.ForeignKey('blogpost',related_name='comment',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    comment=models.TextField(max_length=100)
    published_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def __str__(self):
        return self.comment
    def approved(self):
        self.approved_comment=True
        self.save()
    def get_absolute_url(self): 
        return reverse('postdetail', kwargs={'pk': self.pk})
        