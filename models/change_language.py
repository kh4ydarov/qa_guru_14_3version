import allure
from models.user import user

from selene import browser, be, command, have


class ChangeLanguage:
    def change_language_uzbek(self):
        with allure.step("Смена языка пользователя на Узбекский"):
            browser.element('a.lang[href="/uz"]').click()
            browser.element('.ClosePromo').should(be.visible).should(be.clickable).click()
            browser.element('a.lang[aria-current="page"]').should(have.text("O'Z"))
        return self


    def change_language_english(self):
        with allure.step("Смена языка пользователя на Английский"):
            browser.element('a.lang[href="/en"]').click()
            browser.element('.ClosePromo').should(be.visible).should(be.clickable).click()
            browser.element('a.lang[aria-current="page"]').should(have.text("EN"))
        return self


change_language = ChangeLanguage()