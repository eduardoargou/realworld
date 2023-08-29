from playwright.sync_api import Page, expect

class AuthorProfile:
    # Locators
    content = 'div.profile-page'
    articles = 'div.article-preview'
    favorites = 'a.nav-link[href*="/favorites"]'
    button_follow = 'button.action-btn'

    def __init__(self, page: Page) -> None:
        self.page = page

    def assert_page_loaded(self) -> None:
        expect(self.page.locator(self.content)).to_be_visible()

    def assert_articles_are_visible(self) -> None:
        articles = self.page.locator(self.articles)
        for i in range(articles.count()):
            expect(articles.nth(i)).to_be_visible()

    def open_favorites(self) -> None:
        self.page.locator(self.favorites).click()

    def prepare_unfollow(self) -> None:
        button = self.page.locator(self.button_follow)
        if 'btn-secondary' in button.get_attribute('class'):
            self.unfollow()

    def prepare_follow(self) -> None:
        button = self.page.locator(self.button_follow)
        if 'btn-outline-secondary' in button.get_attribute('class'):
            self.follow()

    def follow(self) -> None:
        button = self.page.locator(self.button_follow)
        with self.page.expect_response('**/toggleFollow') as res:
            button.click()
        assert res.value.status == 200
        assert 'btn-secondary' in button.get_attribute('class')

    def unfollow(self) -> None:
        button = self.page.locator(self.button_follow)
        with self.page.expect_response('**/toggleFollow') as res:
            button.click()
        assert res.value.status == 200
        assert 'btn-outline-secondary' in button.get_attribute('class')
