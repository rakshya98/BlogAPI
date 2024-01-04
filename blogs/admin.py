from django.contrib import admin

from blogs.models import Category,Blog

admin.site.register(Blog)
admin.site.register(Category)