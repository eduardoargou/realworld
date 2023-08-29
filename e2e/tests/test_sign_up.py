from playwright.sync_api import Page
from pages.register import Register

sign_up_url = '/register'

def test_sign_up(page: Page) -> None:
    page.goto(sign_up_url)
    register = Register(page)
    register.fill_username('New Test')
    register.fill_username('newtest@test.com')
    register.fill_password('test123')
    def handle(route):
        json = { 'status': 200 }
        route.fulfill(json=json)
    page.route('**/register', handle)
    register.click_sign_up()
