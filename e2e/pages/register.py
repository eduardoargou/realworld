from playwright.sync_api import Page

class Register:
    # Locators
    input_username = 'input[name="username"]'
    input_email = 'input[name="email"]'
    input_password = 'input[name="password"]'
    button_sign_up = 'button.btn-primary'

    def __init__(self, page: Page) -> None:
        self.page = page

    def fill_username(self, username: str) -> None:
        self.page.locator(self.input_username).fill(username)

    def fill_email(self, email: str) -> None:
        self.page.locator(self.input_email).fill(email)

    def fill_password(self, password: str) -> None:
        self.page.locator(self.input_password).fill(password)

    def click_sign_up(self) -> None:
        self.page.locator(self.button_sign_up).click()
