import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from movies.tests import create_movie

from .models import Article, Tag

# Create your tests here.
def create_tag(name, slug):
    return Tag.objects.create(name=name, slug=slug)


def create_article(title, slug, days, published):
    content = "some content"
    summary = "some summary"
    offset = datetime.timedelta(days)
    pub_date = timezone.now() - offset
    tag1 = create_tag("tag_name1", "tag-slug1")
    tag2 = create_tag("tag_name2", "tag-slug2")
    article = Article.objects.create(
        title=title,
        slug=slug,
        content=content,
        summary=summary,
        pub_date=pub_date,
        published=published,
    )
    article.tags.set([tag1, tag2])
    return article


class BlogIndexTests(TestCase):
    def test_index_with_no_articles(self):
        """If there is no arcticles, display an appropriate text"""
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucun article")

    def test_index_with_past_and_unpublished_article(self):
        """If there's a published article with a pub_date in the past, it should be displayed on the index"""
        create_article(
            "some title", "some-slug-for-the-article", days=2, published=False
        )
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucun article")

    def test_index_with_past_and_published_article(self):
        """If there's a published article with a pub_date in the past, it should be displayed on the index"""
        create_article(
            title="Tartampion",
            slug="tartampion",
            days=1,
            published=True,
        )
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tartampion")
        self.assertContains(response, "tag_name2")

    def test_index_with_future_published_articles(self):
        """In this case the article shouldn't be displayed"""
        create_article(
            title="Tartampion",
            slug="tartampion",
            days=-3,  # negative days offset means the article is published in the future
            published=True,
        )
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucun article")
