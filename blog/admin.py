from django.contrib import admin
from .models import Article, Tag
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(Tag)
admin.site.register(Article, MarkdownxModelAdmin)
