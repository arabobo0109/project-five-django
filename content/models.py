from django.db import models
from django.utils import timezone

class Content(models.Model):
    """
    Rendering the content from a post
    """
    title = models.CharField(max_length=200, default='')
    strapline = models.TextField(default='')
    article = models.TextField(default='')
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image1 = models.ImageField(upload_to="img", blank=True, null=True)
    image2 = models.ImageField(upload_to="img", blank=True, null=True)
    image3 = models.ImageField(upload_to="img", blank=True, null=True)
    image4 = models.ImageField(upload_to="img", blank=True, null=True)

    def __unicode__(self):
        return self.title