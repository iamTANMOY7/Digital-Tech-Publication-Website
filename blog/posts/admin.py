from django.contrib import admin
from .models import Post


@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "post_title", "published_date", "post_authors"]
    list_display_links = ["id", "post_title"]
    list_filter = ["published_date"]
