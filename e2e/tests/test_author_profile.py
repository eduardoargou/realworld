from playwright.sync_api import Page
from pages.author_profile import AuthorProfile
from auth.session import load_session

author_profile_url = None

def load_profile_url(page: Page) -> None:
    global author_profile_url
    if author_profile_url:
        page.goto(author_profile_url)
    else:
        from pages.articles_feed import ArticlesFeed
        page.goto('/')
        feed = ArticlesFeed(page)
        feed.open_first_profile()
        profile = AuthorProfile(page)
        profile.assert_page_loaded()
        author_profile_url = page.url

def test_load_author_feed(page: Page) -> None:
    load_session(page, 'test')
    load_profile_url(page)
    profile = AuthorProfile(page)
    profile.assert_articles_are_visible()

def test_load_favorites(page: Page) -> None:
    load_session(page, 'test')
    load_profile_url(page)
    profile = AuthorProfile(page)
    profile.open_favorites()
    profile.assert_articles_are_visible()

def test_follow_author(page: Page) -> None:
    load_session(page, 'test')
    load_profile_url(page)
    profile = AuthorProfile(page)
    profile.prepare_unfollow()
    profile.follow()

def test_unfollow_author(page: Page) -> None:
    load_session(page, 'test')
    load_profile_url(page)
    profile = AuthorProfile(page)
    profile.prepare_follow()
    profile.unfollow()
