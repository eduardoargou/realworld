from playwright.sync_api import Page, expect

class MyProfile:
    # Locators
    content = 'div.profile-page'
    articles = 'div.article-preview'
    favorites = 'a.nav-link[href*="/favorites"]'

    def __init__(self, page: Page) -> None:
        self.page = page

    def assert_page_loaded(self) -> None:
        expect(self.page.locator(self.content)).to_be_visible()

    def assert_articles_are_visible(self) -> None:
        articles = self.page.locator(self.articles)
        for i in range(articles.count()):
            expect(articles.nth(i)).to_be_visible()

    def open_favorites(self) -> None:
        with self.page.expect_response('**/favorites/*') as res:
            self.page.locator(self.favorites).click()
        assert res.value.status == 200
