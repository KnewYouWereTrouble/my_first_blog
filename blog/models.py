from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User')
    text = models.TextField(default="")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name="comments") #allows us to have access to comments from Post model
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)


    def approve(self):
        self.approve = True
        self.save()

    def flag_as_inappropriate(self):
        self.text = "MODERATOR :: Flag as inappropriate"
        self.save()

    def __str__(self):
        return self.text
