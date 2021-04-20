from django.contrib import admin
from core.models import Post,Comment,Contact,Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Category)