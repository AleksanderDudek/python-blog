from django.contrib import admin
# zeby zarzadzanie modelem bylo dostepne z panelu uprawnien admina
from .models import BlogPost

# Register your models here.

admin.site.register(BlogPost)