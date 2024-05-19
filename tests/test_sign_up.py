from models.test_authorization import authorization
from models.open_page import open_page


def test_sign_up():
    open_page.open_site()
    authorization.sign_up()

