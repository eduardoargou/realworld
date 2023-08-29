from playwright.sync_api import Page
from pages.articles_feed import ArticlesFeed
from auth.session import load_session

def test_load_global_feed(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.assert_articles_are_visible()

def test_like_article(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.prepare_first_article_unliked()
    feed.like_first_article()

def test_unlike_article(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.prepare_first_article_liked()
    feed.unlike_first_article()

def test_filter_by_tag(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.test_random_tag()

def test_load_my_feed(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.open_my_feed()
    feed.assert_articles_are_visible()

def test_open_article(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.open_first_article()
