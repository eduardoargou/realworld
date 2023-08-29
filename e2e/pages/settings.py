from playwright.sync_api import Page

class Settings:
    # Locators
    button_logout = 'button.btn-outline-danger'
    input_bio_text = 'textarea[name="bio"]'
    button_update = 'button.btn-primary'
    button_my_profile = 'a[href*="profile"]'

    def __init__(self, page: Page) -> None:
        self.page = page

    def click_logout(self) -> None:
        self.page.locator(self.button_logout).click()

    def fill_bio(self, bio_text) -> None:
        self.page.locator(self.input_bio_text).click()
        self.page.keyboard.press('Meta+A')
        self.page.keyboard.press('Backspace')
        self.page.locator(self.input_bio_text).fill(bio_text)

    def click_update(self) -> None:
        with self.page.expect_response('**/save') as res:
            self.page.locator(self.button_update).click()
        assert res.value.status == 200

    def click_my_profile(self) -> None:
        self.page.locator(self.button_my_profile).click()
