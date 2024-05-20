import time

import allure

from selene import browser, be, have


class OpenPage:

    def close_promo(self):
        browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
        if browser.element('.ClosePromo').matching(be.visible.and_(be.clickable)):
            browser.element('.ClosePromo').click()
        return

    def open_site(self):
        with allure.step("Открыть сайт allplay.uz"):
            browser.open("")
            browser.element('.ClosePromo').should(be.visible).should(be.clickable).click()
            self.close_promo()
            self.close_promo()


        return self

    def tv_page(self):
        with allure.step("Переход в раздел ТВ"):
            browser.element('a.Navbar__link[href="/tv"]').click()
            self.close_promo()
        return self

    def asserting_tv_page(self):
        with allure.step("Проверка страницы после нажатие кнопки в раздел ТВ"):
            browser.element('.PageSection__title-left').should(have.text('Список каналов'))
        return self

    def authorization_page(self):
        with allure.step("Переход в страницу авторизации"):
            if browser.element('.ClosePromo').matching(be.visible.and_(be.clickable)):
                browser.element('.ClosePromo').click()
                browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
            elif not browser.element('.ClosePromo').matching(be.visible) or not browser.element('.ClosePromo').matching(
                    be.clickable):
                browser.element('a.d-none.d-lg-inline.Navbar__link[href="/login/"]').click()
            # browser.element('a.d-none.d-lg-inline.Navbar__link[href="/login/"]').click()

        return self

    def asserting_auth_page(self):
        with allure.step("Проверка перехода на страницу авторизации после нажатии кнопки Вход"):
            if browser.element('.ClosePromo').matching(be.visible.and_(be.clickable)):
                browser.element('.ClosePromo').click()
                browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
            elif not browser.element('.ClosePromo').matching(be.visible) or not browser.element('.ClosePromo').matching(
                    be.clickable):
                browser.element('.Login__title').should(have.text('Вход'))
            # browser.element('.Login__title').should(have.text('Вход'))
        return self


open_page = OpenPage()
