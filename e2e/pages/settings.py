from playwright.sync_api import Page

class Settings:
    # Locators
    button_logout = 'button.btn-outline-danger'

    def __init__(self, page: Page) -> None:
        self.page = page

    def click_logout(self) -> None:
        self.page.locator(self.button_logout).click()
