from playwright.sync_api import Page, expect

class ViewArticle:
    # Locators
    card_comment = 'div.card'
    remove_comment = 'div.card form.mod-options'
    textarea_comment = 'textarea[name="comment"]'
    button_post = 'button[type="submit"]'

    def __init__(self, page: Page) -> None:
        self.page = page

    def validate_page_has_loaded(self) -> None:
        textarea = self.page.locator(self.textarea_comment)
        expect(textarea).to_be_visible()

    def prepare_no_comments(self) -> None:
        self.validate_page_has_loaded()
        comments = self.page.locator(self.card_comment)
        if comments.count():
            self.delete_comment()

    def prepare_has_comments(self) -> None:
        self.validate_page_has_loaded()
        comments = self.page.locator(self.card_comment)
        if not comments.count():
            self.post_comment()

    def post_comment(self) -> None:
        self.page.locator(self.textarea_comment).fill('test')
        with self.page.expect_response('**/createComment') as res:
            self.page.locator(self.button_post).click()
        assert res.value.status == 200

    def delete_comment(self) -> None:
        with self.page.expect_response('**/deleteComment*') as res:
            self.page.locator(self.remove_comment).nth(0).click()
        assert res.value.status == 200
