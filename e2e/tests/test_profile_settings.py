from playwright.sync_api import Page
from pages.my_profile import MyProfile
from pages.settings import Settings
from auth.session import load_session

settings_url = '/settings'

def generate_bio_text() -> str:
    import random
    i = random.randint(0, 1000000)
    text = f'this is a description {str(i)}'
    return text

def test_edit_profile(page: Page) -> None:
    load_session(page, 'test')
    page.goto(settings_url)
    settings = Settings(page)
    bio_text = generate_bio_text()
    settings.fill_bio(bio_text)
    settings.click_update()
    settings.click_my_profile()
    my_profile = MyProfile(page)
    my_profile.validate_bio_text(bio_text)
