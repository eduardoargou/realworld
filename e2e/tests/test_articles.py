from playwright.sync_api import Page
from pages.new_article import NewArticle
from pages.articles_feed import ArticlesFeed
from pages.view_article import ViewArticle
from auth.session import load_session

new_post_url = '/editor'

def generate_article_text() -> str:
    import random
    i = random.randint(0, 1000000)
    text = f'this is an article {str(i)}'
    return text

def test_post_new_article(page: Page) -> None:
    load_session(page, 'test')
    page.goto(new_post_url)
    new_article = NewArticle(page)
    new_article.fill_in_example()
    def handle(route):
        json = { 'status': 200 }
        route.fulfill(json=json)
    page.route('**/editor', handle)
    new_article.click_publish()

def test_remove_article(page: Page) -> None:
    load_session(page, 'test')
    # Create a new article to remove
    page.goto(new_post_url)
    new_article = NewArticle(page)
    new_article.fill_in_example()
    with page.expect_response('**/editor') as res:
        new_article.click_publish()
    assert res.value.status == 200
    # Remove created article
    article = ViewArticle(page)
    article.remove()

def test_edit_article(page: Page) -> None:
    load_session(page, 'test')
    # Create a new article to edit
    page.goto(new_post_url)
    new_article = NewArticle(page)
    new_article.fill_in_example()
    with page.expect_response('**/editor') as res:
        new_article.click_publish()
    assert res.value.status == 200
    # Edit article
    article = ViewArticle(page)
    article.click_edit()
    body = generate_article_text()
    new_article.fill_body(body)
    with page.expect_response('**/editor*') as res:
        new_article.click_publish()
    assert res.value.status == 200
    article.validate_article_body_text(body)
    # Remove created article
    article.remove()

def test_post_new_article_failure(page: Page) -> None:
    load_session(page, 'test')
    page.goto(new_post_url)
    new_article = NewArticle(page)
    with page.expect_response('**/editor') as res:
        new_article.click_publish()
    body = res.value.json()
    assert body['type'] == 'failure'
    assert body['status'] == 400
