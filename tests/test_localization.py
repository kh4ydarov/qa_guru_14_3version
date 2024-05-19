from models.change_language import change_language
from models.open_page import open_page


def change_languages():
    open_page.open_site()
    change_language.change_language_uzbek()
    change_language.change_language_english()
