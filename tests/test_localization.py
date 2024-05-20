from models.change_language import change_language
from models.open_page import open_page


def test_change_language_uz():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_uzbek()
    change_language.asserting_localization_uz()


def test_change_language_en():
    open_page.open_site()
    open_page.authorization_page()
    change_language.change_language_english()
    change_language.asserting_localization_eng()
