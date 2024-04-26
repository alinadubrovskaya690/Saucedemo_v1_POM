import pytest
import allure
from pages.base_page import BasePage
from locators.auth_locs import AuthLocs, AuthData


@pytest.fixture()
def login(log_page):
    with allure.step('standard user authorization'):
        log_page.auth(AuthData.valid_username1, AuthData.valid_password)

@pytest.fixture()
def locked_out_login(log_page):
    with allure.step('locked out user authorization'):
        log_page.auth(AuthData.valid_username2, AuthData.valid_password)

@pytest.fixture()
def problem_login(log_page):
    with allure.step('problem user authorization'):
        log_page.auth(AuthData.valid_username3, AuthData.valid_password)

@pytest.fixture()
def glitch_login(log_page):
    with allure.step('performance glitch user authorization'):
        log_page.auth(AuthData.valid_username4, AuthData.valid_password)

class LogPage(BasePage):
    def input_user(self):
        return self.is_visible(AuthLocs.user_field)

    def fill_input_user(self, username):
        return self.is_visible(AuthLocs.user_field).send_keys(username)

    def input_pass(self):
        return self.is_visible(AuthLocs.password_field)

    def fill_input_pass(self, password):
        return self.is_visible(AuthLocs.password_field).send_keys(password)

    def login_btn(self):
        return self.is_clickable(AuthLocs.login_button)

    def click_login_btn(self):
        return self.is_clickable(AuthLocs.login_button).click()

    def auth(self, username, password):
        self.open()
        self.fill_input_user(username)
        self.fill_input_pass(password)
        self.click_login_btn()
        return self

    @staticmethod
    def locked_message():
        return AuthData.auth_locked_message

    @staticmethod
    def error_message1():
        return AuthData.auth_error_message1

    @staticmethod
    def error_message2():
        return AuthData.auth_error_message2

    @staticmethod
    def error_message3():
        return AuthData.auth_error_message3