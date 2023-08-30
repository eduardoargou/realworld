from playwright.sync_api import Page
from pages.articles_feed import ArticlesFeed
from pages.view_article import ViewArticle
from auth.session import load_session

def test_post_comment(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.open_first_article()
    article = ViewArticle(page)
    article.prepare_no_comments()
    article.post_comment()

def test_delete_comment(page: Page) -> None:
    load_session(page, 'test')
    page.goto('/')
    feed = ArticlesFeed(page)
    feed.open_first_article()
    article = ViewArticle(page)
    article.prepare_has_comments()
    article.delete_comment()
