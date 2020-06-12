from store.models import Category
from django.urls import reverse

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)