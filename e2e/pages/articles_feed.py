from playwright.sync_api import Page, expect

class ArticlesFeed:
    # Locators
    articles = 'div.article-preview'
    button_like = 'button.btn-sm'
    tags = 'a.tag-pill'
    my_feed = 'a.nav-link[href="/?tab=feed"]'
    article_link = 'a.preview-link > h1'

    def __init__(self, page: Page) -> None:
        self.page = page
    
    def assert_articles_are_visible(self) -> None:
        articles = self.page.locator(self.articles)
        for i in range(articles.count()):
            expect(articles.nth(i)).to_be_visible()

    def prepare_first_article_unliked(self) -> None:
        button = self.page.locator(self.button_like).nth(0)
        if 'btn-primary' in button.get_attribute('class'):
            self.unlike_first_article()

    def prepare_first_article_liked(self) -> None:
        button = self.page.locator(self.button_like).nth(0)
        if 'btn-outline-primary' in button.get_attribute('class'):
            self.like_first_article()

    def like_first_article(self) -> None:
        button = self.page.locator(self.button_like).nth(0)
        with self.page.expect_response('**/article/*') as res:
            button.click()
        assert res.value.status == 200
        assert 'btn-primary' in button.get_attribute('class')

    def unlike_first_article(self) -> None:
        button = self.page.locator(self.button_like).nth(0)
        with self.page.expect_response('**/article/*') as res:
            button.click()
        assert res.value.status == 200
        assert 'btn-outline-primary' in button.get_attribute('class')

    def test_random_tag(self) -> None:
        tags = self.page.locator(self.tags)
        import random
        tag = tags.nth(random.randint(0, tags.count() - 1))
        tag_text = tag.get_attribute('href')[2:]
        with self.page.expect_response(f'**/__data.json?{tag_text}*') as res:
            tag.click()
        assert res.value.status == 200

    def open_my_feed(self) -> None:
        self.page.locator(self.my_feed).click()

    def open_first_article(self) -> None:
        with self.page.expect_response('**/article/*') as res:
            self.page.locator(self.article_link).nth(0).click()
        assert res.value.status == 200
