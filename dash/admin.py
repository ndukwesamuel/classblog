from django.contrib import admin

# Register your models here.
from .models import post,Comment,category
#  Job_post,Company,File

# Register your models here.


# admin.site.register(Profile)
admin.site.register(post)
admin.site.register(Comment)
admin.site.register(category)
