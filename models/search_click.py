import allure

from selene import browser, be, have, command


class Search:

    def search_elements(self):
        with allure.step("Поиск определленого фильма и переход в карточку фильма"):
            browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
            if browser.element('.ClosePromo').matching(be.visible.and_(be.clickable)):
                browser.element('.ClosePromo').click()
            browser.element('a.Navbar__link[aria-label="Поиск"]').click()
            browser.element('.search-bar').should(be.visible).should(be.clickable).click()
            browser.element('.input').set_value('Терминатор').press_enter()
            browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
            browser.element('.SearchResults__title').perform(command.js.scroll_into_view)
        return self

    def asserting_result(self):
        with allure.step("Проверка на результать поиска фильма"):
            browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
            browser.element('.SearchResults__title').should(have.text('Фильмы'))
        return self


search = Search()
