from django.contrib import admin

# Register your models here.
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["headline", "reporter", "publish"]
    list_filter = ["publish", "reporter"]
    search_fields = ["headline", "content"]
    raw_id_fields = ["reporter"]
    date_hierarchy = "publish"
    ordering = ["publish"]
