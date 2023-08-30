from playwright.sync_api import Page

class NewArticle:
    # Locators
    input_title = 'input[name="title"]'
    input_description = 'input[name="description"]'
    textarea_body = 'textarea[name="body"]'
    input_tags = 'input[placeholder="Enter tags"]'
    button_publish = 'button.btn-primary'

    def __init__(self, page: Page) -> None:
        self.page = page

    def fill_title(self, text: str) -> None:
        self.page.locator(self.input_title).fill(text)

    def fill_description(self, text: str) -> None:
        self.page.locator(self.input_description).fill(text)

    def fill_body(self, text: str) -> None:
        self.page.locator(self.textarea_body).fill(text)

    def fill_tags(self, text: str) -> None:
        self.page.locator(self.input_tags).fill(text)

    def fill_in_example(self) -> None:
        self.fill_title('Testing')
        self.fill_description('Description')
        self.fill_body('Hello World!')
        self.fill_tags('test')

    def click_publish(self) -> None:
        self.page.locator(self.button_publish).click()
