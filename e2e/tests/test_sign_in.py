from playwright.sync_api import Page
from pages.sign_in import SignIn

sign_in_url = 'https://realworld.svelte.dev/login'
user_email = 'automated@test.dev'
user_password = 'automatedtest'
wrong_password = 'wrongpassword'

def test_sign_in_success(page: Page) -> None:
    page.goto(sign_in_url)
    sign_in = SignIn(page)
    sign_in.fill_email(user_email)
    sign_in.fill_password(user_password)
    with page.expect_response('**/login') as res:
        sign_in.click_sign_in()
    assert res.value.status == 200

def test_sign_in_error(page: Page) -> None:
    page.goto(sign_in_url)
    sign_in = SignIn(page)
    sign_in.fill_email(user_email)
    sign_in.fill_password(wrong_password)
    with page.expect_response('**/login') as res:
        sign_in.click_sign_in()
    assert res.value.status == 403
