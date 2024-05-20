import time

import allure

from selene import browser, be, have


class OpenPage:

    def open_site(self):
        with allure.step("Открыть сайт allplay.uz"):
            browser.open("")
            time.sleep(5)
            browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
            browser.element('.ClosePromo').should(be.visible).should(be.clickable).click()
        return self

    def tv_page(self):
        with allure.step("Переход в раздел ТВ"):
            browser.element('a.Navbar__link[href="/tv"]').click()
        return self

    def asserting_tv_page(self):
        with allure.step("Проверка страницы после нажатие кнопки в раздел ТВ"):
            browser.element('.PageSection__title-left').should(have.text('Список каналов'))
        return self

    def authorization_page(self):
        with allure.step("Переход в страницу авторизации"):
            browser.element('a.d-none.d-lg-inline.Navbar__link[href="/login/"]').click()
        return self

    def asserting_auth_page(self):
        with allure.step("Проверка перехода на страницу авторизации после нажатии кнопки Вход"):
            browser.element('.Login__title').should(have.text('Вход'))
        return self


open_page = OpenPage()
