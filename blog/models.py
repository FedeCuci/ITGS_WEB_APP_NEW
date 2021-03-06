from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
#    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_top_level_comments(self):
        return self.comment_set.filter(reply__isnull=True)

class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True, related_name='replies')

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.author.username))

#    def get_absolute_url(self):
 #       return reverse('post-detail', kwargs={'pk': self.post.pk})
