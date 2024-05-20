import allure

from test_data.data import user

from selene import browser, command, have, be


class Authorization:
    def sign_up(self):
        with allure.step("Регистрация нового пользователя"):
            browser.element('.Login__link').click()
            browser.element('#referralId').perform(command.js.scroll_into_view).click()
            browser.element('#name').set_value(user.name)
            browser.element('#email').set_value(user.email)
            browser.element('#password').set_value(user.password)
            browser.element('#confirmPassword').set_value(user.confirm_password)
            browser.element('#remember').click()
            browser.element('.Login__submit').click()
        return self

    def asserting_sign_up(self):
        with allure.step("Проверка перехода на страницу Подтверждение кода"):
            browser.element('#code').should(have.text('Код подтверждения'))
        return self


    def sign_in(self):
        with allure.step("Авторизация с валидными данными"):
            browser.element('#email').set_value(user.sign_in_login)
            browser.element('#password').set_value(user.sign_in_password)
            browser.element('.Login__button').click()
        return self

    def asserting_sign_in(self):
        with allure.step("Успешная авторизация"):
            browser.should(have.js_returned(True, 'return document.readyState === "complete"'))
            browser.element('.UserMenu').should(be.present)
        return self


authorization = Authorization()
