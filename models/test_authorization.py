import allure
from models.user import user

from selene import browser, be, command


class Authorization:
    def sign_up(self):
        with allure.step("Регистрация нового пользователя"):
            browser.element('.Login__link').click()
            browser.element('#referralId').perform(command.js.scroll_into_view).click()
            browser.element('#name').set_value(user.name)
            browser.element('#email').set_value(user.email)
            browser.element('#password').set_value(user.password)
            browser.element('#confirmPassword').set_value(user.confirm_password)
            browser.element('.remember').click()
            browser.element('.Login__submit').click()
        return self

    def sign_in(self):
        with allure.step("Авторизация с валидными данными"):
            browser.element('#email').set_value(user.email)
            browser.element('#password').set_value(user.password)
            browser.element('.Login__button').click()
        return self


authorization = Authorization()
