from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Rendering a post on the blog
    """
    title = models.CharField(max_length=30, default='')
    content = models.CharField(max_length=500, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey(User, default="")
    status_choice = (
        ('PR', 'In Progress'),
        ('PL', 'In Planning'),
        ('C', 'Completed'),
        ('W', 'Waiting to be Funded'),
        ('R', 'Recently Submitted'),
    )
    status = models.CharField(max_length=2, choices=status_choice, default='R')
    votes = models.IntegerField(default = 0)
    image = models.ImageField(upload_to="img", blank=True, null=True, default='')

    
    def __unicode__(self):
        return self.title