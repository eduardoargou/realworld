from playwright.sync_api import Page
from pages.settings import Settings
from auth.session import load_session

settings_url = '/settings'

def test_sign_out(page: Page) -> None:
    load_session(page, 'test')
    page.goto(settings_url)
    settings = Settings(page)
    with page.expect_response('**/logout') as res:
        settings.click_logout()
    assert res.value.status == 200
