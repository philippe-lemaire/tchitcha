from datetime import time
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.contrib import admin

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=35)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    content = MarkdownxField()
    summary = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="articles")

    def __str__(self):
        return self.title

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    @admin.display(
        ordering="pub_date",
        description="Published?",
        boolean=True,
    )
    def is_published(self):
        return self.published
