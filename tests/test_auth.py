import pytest
import requests
import allure

from pages.auth_page import locked_out_login, problem_login, glitch_login
from locators.auth_locs import AuthLocs, AuthData
from locators.urls import URLs

@allure.id('1.1')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('standard user authorization')
@pytest.mark.positive
def test_auth_positive(browser, login, inv_page):
    with allure.step('check the current url, the page header and the items presence on the inventory page'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.prod_lab().text == 'Products', 'Wrong page header'
        assert len(inv_page.inventory_cards()) > 0, 'No item cards'

    print(f'\nStandard user...')

@allure.id('1.2')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('locked out user authorization')
@pytest.mark.positive
def test_auth_positive_locked_out_user(browser, locked_out_login, log_page):
    with allure.step('check the current url, the page header and the items presence on the inventory page'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.locked_message() == AuthData.auth_locked_message, 'Login error'

    print(f'\nLocked out user... {log_page.locked_message()}')

@allure.id('1.3')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('problem user authorization')
@pytest.mark.positive
def test_auth_positive_problem_user(browser, problem_login, inv_page):
    with allure.step('check the current url, the page header and the items presence on the inventory page'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.prod_lab().text == 'Products', 'Wrong page header'
        assert len(inv_page.inventory_cards()) > 0, 'No item cards'

    print(f'\nProblem user...')

@allure.id('1.4')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('performance glitch user authorization')
@pytest.mark.positive
def test_auth_positive_glitch_user(browser, glitch_login, inv_page):
    with allure.step('check the current url, the page header and the items presence on the inventory page'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.prod_lab().text == 'Products', 'Wrong page header'
        assert len(inv_page.inventory_cards()) > 0, 'No item cards'

    print(f'\nGlitch user...')

@allure.id('1.5')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('invalid data authorization')
@pytest.mark.negative
def test_auth_negative_invalid_login(browser, log_page):

    log_page.open()
    with allure.step('log in with invalid data'):
        log_page.input_user().send_keys(AuthData.invalid_username)
        log_page.input_pass().send_keys(AuthData.invalid_password)
        log_page.login_btn().click()

    with allure.step('check the current url and the error message is provided'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.error_message3() == AuthData.auth_error_message3, 'Login error'

    print(f'\nWrong login user... {log_page.error_message3()}')

@allure.id('1.6')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('empty fields authorization')
@pytest.mark.negative
def test_auth_negative_empty_fields(browser, log_page):

    log_page.open()
    with allure.step('log in with empty fields'):
        log_page.login_btn().click()

    with allure.step('check the current url and the error message is provided'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.error_message1() == AuthData.auth_error_message1, 'Login error'

    print(f'\nEmpty login user... {log_page.error_message1()}')

@allure.id('1.7')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('empty username authorization')
@pytest.mark.negative
def test_auth_negative_empty_username_field(browser, log_page):

    log_page.open()
    with allure.step('log in with the empty username field'):
        log_page.input_user().send_keys(AuthData.valid_password)
        log_page.login_btn().click()

    with allure.step('check the current url and the error message is provided'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.error_message1() == AuthData.auth_error_message1, 'Login error'

    print(f'\nEmpty username login user... {log_page.error_message2()}')

@allure.id('1.8')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('empty password authorization')
@pytest.mark.negative
def test_auth_negative_empty_password_field(browser, log_page):

    log_page.open()
    with allure.step('log in with the empty password field'):
        log_page.input_user().send_keys(AuthData.valid_username1)
        log_page.login_btn().click()

    with allure.step('check the current url and the error message is provided'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'
        assert log_page.error_message2() == AuthData.auth_error_message2, 'Login error'

    print(f'\nEmpty password login user... {log_page.error_message2()}')