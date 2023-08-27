from pages.sign_in import SignIn

sign_in_url = 'https://realworld.svelte.dev/login'

def test_sign_in_success(page):
    sign_in = SignIn(page)
    sign_in.page.goto(sign_in_url)
    assert False

def test_sign_in_error(page):
    sign_in = SignIn(page)
    sign_in.page.goto(sign_in_url)
    assert False
