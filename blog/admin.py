from django.contrib import admin
from .models import Article, Tag
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.


class ArticleAdmin(MarkdownxModelAdmin):
    list_display = [
        "title",
        "is_published",
        "pub_date",
    ]
    list_filter = ["pub_date"]


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
