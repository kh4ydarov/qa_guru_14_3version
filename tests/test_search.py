from models.search_click import search
from models.open_page import open_page


def test_search():
    open_page.open_site()
    search.search_elements()
    search.asserting_result()
