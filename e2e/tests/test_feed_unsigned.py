from playwright.sync_api import Page
from pages.articles_feed import ArticlesFeed

def test_load_global_feed_unsigned(page: Page) -> None:
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.assert_articles_are_visible()

def test_filter_by_tag_unsigned(page: Page) -> None:
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.test_random_tag()

def test_open_article_unsigned(page: Page) -> None:
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.open_first_article()

def test_open_profile_unsigned(page: Page) -> None:
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.open_first_profile()
