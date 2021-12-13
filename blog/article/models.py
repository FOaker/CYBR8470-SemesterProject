from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


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

    total_views = models.PositiveIntegerField(default=0)

    class Meta:
        # reverse order
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])