from django.contrib import admin

# Register your models here.
from .models import  AuthorModel,BlogModel

admin.site.register(AuthorModel)
admin.site.register(BlogModel)
