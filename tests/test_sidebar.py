import pytest
import allure
from pages.auth_page import login
from locators.urls import URLs
from locators.items_locs import ItemData

@allure.id('5.1')
@allure.epic('sidebar page')
@allure.feature('sidebar')
@allure.title('logout button')
@pytest.mark.positive
def test_logout(browser, login, log_page, menu_page):
    with allure.step('click the sidebar button'):
        menu_page.sidebar_menu().click()

    with allure.step('click the logout button'):
        menu_page.sidebar_logout().click()

    with allure.step('check if we are on the login page and the login button appears'):
        assert browser.current_url == URLs.auth_url, 'Wrong URL'

        log_btn = log_page.login_btn()
        assert log_page.login_btn(), "Login button doesn't appear"
        assert log_btn.get_attribute('value') == 'LOGIN', 'Login button not found'

@allure.id('5.2')
@allure.epic('sidebar page')
@allure.feature('sidebar')
@allure.title('about button')
@pytest.mark.positive
def test_about(browser, login, menu_page, about_page):
    with allure.step('click the sidebar button'):
        menu_page.sidebar_menu().click()

    with allure.step('click the about button'):
        menu_page.sidebar_about().click()

    with allure.step('check the expected url'):
        curr_title = browser.title
        assert browser.current_url == URLs.about_url and \
            curr_title == about_page.exp_title(), 'Wrong URL or title'

@allure.id('5.3')
@allure.epic('sidebar page')
@allure.feature('sidebar')
@allure.title('all items button')
@pytest.mark.positive
def test_all_items(browser, login, menu_page, inv_page, item_page):
    with allure.step('enter the item page'):
        inv_page.inventory_names()[2].click()
        assert browser.current_url == URLs.item3_url, 'Wrong URL'
        assert item_page.items_img().get_attribute('src') == ItemData.item3_img, 'Different item pictures'
        assert item_page.items_desc().text == ItemData.item3_desc, 'Different item descriptions'
        assert item_page.items_price().text == ItemData.item3_price, 'Different item prices'

    with allure.step('click the sidebar button'):
        menu_page.sidebar_menu().click()

    with allure.step('click the all items button'):
        menu_page.sidebar_all_items().click()
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'

@allure.id('5.4')
@allure.epic('sidebar page')
@allure.feature('sidebar')
@allure.title('reset app state button')
@pytest.mark.positive
def test_reset(browser, login, inv_page, cart_page, menu_page):
    with allure.step('add items via the inventory page'):
        inv_page.inventory_add_items()[1].click()
        inv_page.inventory_add_items()[2].click()

        assert int(cart_page.cart_count().text) == 2, 'Wrong items quantity in cart'

    with allure.step('click the sidebar button'):
        menu_page.sidebar_menu().click()

    with allure.step('click the reset app state button'):
        menu_page.sidebar_reset().click()
        assert cart_page.cart_count_invisible(), 'Tag is visible, cart is not empty'

    cart_page.refresh()