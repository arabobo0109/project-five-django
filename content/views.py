from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Content


def get_content(request):
    """
    A view that will return a list of posts that were published
    prior to 'now' and render these to the 'contents.html'.
    """
    contents = Content.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "content.html", {'contents': contents})
    
    
def content_detail(request, pk):
    """
    Returns content based on ID and renders it to the 'contentdetail.html'
    template, or returns a 404 error if the post cannot be found
    """
    content = get_object_or_404(Content, pk=pk)
    content.views += 1
    content.save()
    return render(request, "contentdetail.html", {'content': content})
