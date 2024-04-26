import pytest
import allure

from pages.auth_page import login
from locators.urls import URLs
from locators.items_locs import ItemData

@allure.id('2.1')
@allure.epic('item page')
@allure.feature('item')
@allure.title('adding and removing the item via the item page')
@pytest.mark.positive
def test_item_ip1(browser, login, inv_page, item_page, cart_page):
    with allure.step('enter the item page via the item image'):
        inv_page.inventory_imgs()[1].click()
        assert browser.current_url == URLs.item2_url, 'Wrong URL'
        assert item_page.items_name().text == ItemData.item2_name, 'Different item names'
        assert item_page.items_desc().text == ItemData.item2_desc, 'Different item descriptions'
        assert item_page.items_price().text == ItemData.item2_price, 'Different item prices'
    with allure.step('add the item via the item page'):
        item_page.item_add().click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'
    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong items quantity in cart'
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item names'
    with allure.step('going back to the item page'):
        item_page.back()
    with allure.step('remove the item via the item page'):
        item_page.item_remove().click()
        assert cart_page.cart_count_invisible(), 'Wrong quantity'

@allure.id('2.2')
@allure.epic('item page')
@allure.feature('item')
@allure.title('adding the item via the inventory page and removing the item via the cart page')
@pytest.mark.positive
def test_item_ip2(browser, login, inv_page, item_page, cart_page):
    with allure.step('enter the item page via the item name'):
        inv_page.inventory_names()[1].click()
        assert browser.current_url == URLs.item2_url, 'Wrong URL'
        assert item_page.items_img().get_attribute('src') == ItemData.item2_img, 'Different item pictures'
        assert item_page.items_desc().text == ItemData.item2_desc, 'Different item descriptions'
        assert item_page.items_price().text == ItemData.item2_price, 'Different item prices'
    with allure.step('add the item via the item page'):
        item_page.item_add().click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'
    with allure.step('going to the cart page'):
        cart_page.cart_btn().click()
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong items quantity in cart'
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item names'
    with allure.step('remove the item via the cart page'):
        cart_page.cart_remove_item().click()
        assert cart_page.cart_count_invisible(), 'Wrong quantity'

@allure.id('2.3')
@allure.epic('item page')
@allure.feature('item')
@allure.title('adding and removing the item via the inventory page')
@pytest.mark.positive
def test_item_mp(browser, login, inv_page, item_page, cart_page):
    with allure.step('enter the item page via the item page'):
        inv_page.inventory_add_items()[1].click()
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert inv_page.inventory_names()[1].text == ItemData.item2_name, 'Different item names'
        assert inv_page.inventory_prices()[1].text == ItemData.item2_price, 'Different item prices'
        assert inv_page.inventory_imgs()[1].get_attribute('src') == ItemData.item2_img, 'Different item pictures'
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'
    with allure.step('going to the cart page'):
        cart_page.cart_btn().click()
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong items quantity in cart'
        assert browser.current_url == URLs.cart_url, 'Wrong URL'
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item names'
    with allure.step('going back to the inventory page'):
        cart_page.cart_return_to_shop().click()
    with allure.step('remove the item via the inventory page'):
        inv_page.inventory_remove_items()[0].click()
        assert cart_page.cart_count_invisible(), 'Wrong quantity'