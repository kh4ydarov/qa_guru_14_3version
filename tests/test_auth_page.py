from models.open_page import open_page


def test_auth_page():
    open_page.open_site()
    open_page.authorization_page()
    open_page.asserting_auth_page()

