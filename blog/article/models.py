from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Blog post data model
class ArticlePost(models.Model):
    # Article author
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Article title
    title = models.CharField(max_length=100)

    # Article body
    body = models.TextField()

    # Article creation time
    created = models.DateTimeField(default=timezone.now)

    # Article update time
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # reverse order
        ordering = ('-created',)

    def __str__(self):
        return self.title