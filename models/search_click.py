import allure

from selene import browser, be, have, command


class Search:

    def search_elements(self):
        with allure.step("Поиск определленого фильма и переход в карточку фильма"):
            browser.element('a.Navbar__link[aria-label="Поиск"]').click()
            browser.element('.search-bar').should(be.visible).should(be.clickable).click()
            browser.element('.input').set_value('Терминатор')
            browser.element('.marquee-text__scroll').perform(command.js.scroll_into_view).click()
            browser.element('.marquee-text__scroll').should(have.text('Терминатор'))
        return self


search = Search()
