import allure

from selene import browser, be


class OpenPage:

    def open_site(self):
        with allure.step("Открыть сайт allplay.uz"):
            browser.open("")
            browser.element('.ClosePromo').should(be.visible).should(be.clickable).click()
        return self

    def tv_page(self):
        with allure.step("Переход в раздел ТВ"):
            browser.element('a.Navbar__link[href="/tv"]').click()
        return self

    def movie_page(self):
        with allure.step("Переход в раздел Кинотеатр"):
            browser.element('a.Navbar__link[href="/movies"]').click()
        return self

    def authorization_page(self):
        with allure.step("Переход в страницу авторизации"):
            browser.element('a.d-none.d-lg-inline.Navbar__link[href="/login/"]').click()
        return self


open_page = OpenPage()
