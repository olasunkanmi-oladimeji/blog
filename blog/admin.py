from django.contrib import admin
from .models import blogpost,commentpost
# Register your models here.
admin.site.register(blogpost)
admin.site.register(commentpost)