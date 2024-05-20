from models.test_authorization import authorization
from models.open_page import open_page


def test_sign_in():
    open_page.open_site()
    authorization.sign_in()
    authorization.asserting_sign_in()
