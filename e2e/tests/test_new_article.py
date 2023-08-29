from playwright.sync_api import Page
from pages.new_article import NewArticle
from auth.session import load_session

new_post_url = '/editor'

def test_post_new_article(page: Page) -> None:
    load_session(page, 'test')
    page.goto(new_post_url)
    new_article = NewArticle(page)
    new_article.fill_title('Testing')
    new_article.fill_description('Description')
    new_article.fill_body('Hello World!')
    new_article.fill_tags('test')
    def handle(route):
        json = { 'status': 200 }
        route.fulfill(json=json)
    page.route('**/editor', handle)
    new_article.click_publish()
