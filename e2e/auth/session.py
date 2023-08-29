from playwright.sync_api import Page
from pages.sign_in import SignIn

sign_in_url = '/login'

users = {
    'test': {
        'email': 'automated@test.dev',
        'password': 'automatedtest',
        'cookie': None
    }
}

def load_session(page: Page, user_name: str) -> None:
    user = users[user_name]
    if user['cookie']:
        page.context.add_cookies(user['cookie'])
    else:
        page.goto(sign_in_url)
        sign_in = SignIn(page)
        sign_in.fill_email(user['email'])
        sign_in.fill_password(user['password'])
        with page.expect_response('**/login') as res:
            sign_in.click_sign_in()
        assert res.value.status == 200
        user['cookie'] = page.context.cookies()
