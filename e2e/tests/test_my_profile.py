from playwright.sync_api import Page
from pages.my_profile import MyProfile
from auth.session import load_session

my_profile_url = None

def load_my_profile(page: Page) -> None:
    global my_profile_url
    if my_profile_url:
        page.goto(my_profile_url)
    else:
        from pages.articles_feed import ArticlesFeed
        page.goto('/')
        feed = ArticlesFeed(page)
        feed.open_my_profile()
        profile = MyProfile(page)
        profile.assert_page_loaded()
        my_profile_url = page.url

def test_load_author_feed(page: Page) -> None:
    load_session(page, 'test')
    load_my_profile(page)
    profile = MyProfile(page)
    profile.assert_articles_are_visible()

def test_load_favorites(page: Page) -> None:
    load_session(page, 'test')
    load_my_profile(page)
    profile = MyProfile(page)
    profile.open_favorites()
    profile.assert_articles_are_visible()
