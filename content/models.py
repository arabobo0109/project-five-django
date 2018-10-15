from django.db import models
from django.utils import timezone

class Content(models.Model):
    """
    Rendering the content from a post
    """
    title = models.CharField(max_length=200)
    article = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    # image1 = models.ImageField(upload_to="img", blank=True, null=True)
    # image2 = models.ImageField(upload_to="img", blank=True, null=True)
    # image3 = models.ImageField(upload_to="img", blank=True, null=True)
    # image4 = models.ImageField(upload_to="img", blank=True, null=True)
    # image5 = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title