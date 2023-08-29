from playwright.sync_api import Page

class SignIn:
    # Locators
    input_email = 'input[name="email"]'
    input_password = 'input[name="password"]'
    button_submit = 'button[type="submit"]'

    def __init__(self, page: Page) -> None:
        self.page = page

    def fill_email(self, email: str) -> None:
        self.page.locator(self.input_email).fill(email)

    def fill_password(self, password: str) -> None:
        self.page.locator(self.input_password).fill(password)

    def click_sign_in(self) -> None:
        self.page.locator(self.button_submit).click()
