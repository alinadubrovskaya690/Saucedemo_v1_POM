import pytest
import allure
from pages.auth_page import login
from locators.urls import URLs
from locators.items_locs import ItemData
from locators.order_locs import OrderData

@allure.id('4.1')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order one item with valid data')
@pytest.mark.positive
def test_item_order_ok(browser, login, inv_page, cart_page, order_page):
    with allure.step('add the item via the inventory page'):
        inv_page.inventory_add_items()[1].click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[0].text) == float(ItemData.item2_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('fill the order form with the valid data'):
        order_page.checkout_btn().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'
        order_page.input_fname().send_keys(OrderData.valid_fname)
        order_page.input_lname().send_keys(OrderData.valid_lname)
        order_page.input_zip().send_keys(OrderData.valid_postal)

    with allure.step('enter the order confirmation page'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step2_url, 'Wrong URL'
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert cart_page.cart_item_prices()[0].text == ItemData.item2_price, 'Different item price'
        assert int(order_page.order_item_quantities()[0].text) == 1, 'Wrong items quantity in cart'

    with allure.step('check if the item information is correct'):
        items_sum = float(order_page.subtotal().text.lstrip('Item total: $'))
        assert items_sum == float(ItemData.item2_price.lstrip('$'))
        tax_sum = round(items_sum * OrderData.tax_rate, 2)
        assert tax_sum == float(order_page.tax().text.lstrip('Tax: $'))
        total_sum = float(order_page.total().text.lstrip('Total: $'))
        assert total_sum == round(items_sum + tax_sum, 2), 'Wrong total price'

    with allure.step('enter the order success page'):
        order_page.finish_btn().click()
        assert browser.current_url == URLs.checkout_complete_url and order_page.success_msg(), \
            'Wrong URL, success message is not shown'
        assert order_page.success_img().get_attribute('src') == OrderData.order_success_image, 'Wrong image'
        assert cart_page.cart_count_invisible(), 'Cart is not empty'
        assert len(cart_page.cart_item_names()) == 0, f'{len(cart_page.cart_item_names())} items in cart'

@allure.id('4.2')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order several items with valid data')
@pytest.mark.positive
def test_items_order(browser, login, inv_page, cart_page, order_page):
    with allure.step('add items via the inventory page'):
        inv_page.inventory_add_items()[1].click()
        inv_page.inventory_add_items()[2].click()
        inv_page.inventory_add_items()[3].click()
        assert int(cart_page.cart_count().text) == 3, 'Wrong quantity'

    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[0].text) == float(ItemData.item2_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

        assert cart_page.cart_item_names()[1].text == ItemData.item4_name, 'Different item name'
        assert cart_page.cart_item_descs()[1].text == ItemData.item4_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[1].text) == float(ItemData.item4_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

        assert cart_page.cart_item_names()[2].text == ItemData.item6_name, 'Different item name'
        assert cart_page.cart_item_descs()[2].text == ItemData.item6_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[2].text) == float(ItemData.item6_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('fill the order form with the valid data'):
        order_page.checkout_btn().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'
        order_page.input_fname().send_keys(OrderData.valid_fname)
        order_page.input_lname().send_keys(OrderData.valid_lname)
        order_page.input_zip().send_keys(OrderData.valid_postal)

    with allure.step('enter the order confirmation page'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step2_url, 'Wrong URL'
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert cart_page.cart_item_prices()[0].text == ItemData.item2_price, 'Different item price'
        assert int(order_page.order_item_quantities()[0].text) == 1, 'Wrong items quantity in cart'

        assert cart_page.cart_item_names()[1].text == ItemData.item4_name, 'Different item name'
        assert cart_page.cart_item_descs()[1].text == ItemData.item4_desc, 'Different item description'
        assert cart_page.cart_item_prices()[1].text == ItemData.item4_price, 'Different item price'
        assert int(order_page.order_item_quantities()[1].text) == 1, 'Wrong items quantity in cart'

        assert cart_page.cart_item_names()[2].text == ItemData.item6_name, 'Different item name'
        assert cart_page.cart_item_descs()[2].text == ItemData.item6_desc, 'Different item description'
        assert cart_page.cart_item_prices()[2].text == ItemData.item6_price, 'Different item price'
        assert int(order_page.order_item_quantities()[2].text) == 1, 'Wrong items quantity in cart'

    with allure.step('check if the item information is correct'):
        items_sum = float(order_page.subtotal().text.lstrip('Item total: $'))
        assert items_sum == float(ItemData.item2_price.lstrip('$')) + float(ItemData.item4_price.lstrip('$')) + \
               float(ItemData.item6_price.lstrip('$'))
        tax_sum = round(items_sum * OrderData.tax_rate, 2)
        assert tax_sum == float(order_page.tax().text.lstrip('Tax: $'))
        total_sum = float(order_page.total().text.lstrip('Total: $'))
        assert total_sum == round(items_sum + tax_sum, 2), 'Wrong total price'

    with allure.step('enter the order success page'):
        order_page.finish_btn().click()
        assert browser.current_url == URLs.checkout_complete_url and order_page.success_msg(), \
            'Wrong URL, success message is not shown'
        assert order_page.success_img().get_attribute('src') == OrderData.order_success_image, 'Wrong image'
        assert cart_page.cart_count_invisible(), 'Cart is not empty'
        assert len(cart_page.cart_item_names()) == 0, f'{len(cart_page.cart_item_names())} items in cart'

@allure.id('4.3')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order an empty item with valid data')
@pytest.mark.defect
@pytest.mark.positive
def test_empty_item_order(browser, login, inv_page, cart_page, order_page):
    with allure.step('enter the cart page'):
        assert browser.current_url == URLs.inventory_url, 'Wrong URL'
        assert cart_page.cart_count_invisible(), 'Wrong quantity'

        cart_page.cart_btn().click()
        assert browser.current_url == URLs.cart_url, 'Wrong URL'

    with allure.step('fill the order form with the valid data'):
        cart_page.cart_checkout().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'
        order_page.input_fname().send_keys(OrderData.valid_fname)
        order_page.input_lname().send_keys(OrderData.valid_lname)
        order_page.input_zip().send_keys(OrderData.valid_postal)

    with allure.step('enter the order confirmation page'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step2_url, 'Wrong URL'

    with allure.step('check if the item information is correct'):
        items_sum = float(order_page.subtotal().text.lstrip('Item total: $'))
        assert items_sum == 0
        tax_sum = round(items_sum * OrderData.tax_rate, 2)
        assert tax_sum == float(order_page.tax().text.lstrip('Tax: $'))
        total_sum = float(order_page.total().text.lstrip('Total: $'))
        assert total_sum == round(items_sum + tax_sum, 2), 'Wrong total price'

    with allure.step('enter the order success page'):
        order_page.finish_btn().click()
        assert browser.current_url == URLs.checkout_complete_url and order_page.success_msg(), \
            'Wrong URL, success message is not shown'
        assert order_page.success_img().get_attribute('src') == OrderData.order_success_image, 'Wrong image'
        assert cart_page.cart_count_invisible(), 'Cart is not empty'
        assert len(cart_page.cart_item_names()) == 0, f'{len(cart_page.cart_item_names())} items in cart'

@allure.id('4.4')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order one item with invalid data')
@pytest.mark.defect
@pytest.mark.positive
def test_item_order_wrong(browser, login, inv_page, cart_page, order_page):
    with allure.step('add items via the inventory page'):
        inv_page.inventory_add_items()[0].click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert cart_page.cart_item_names()[0].text == ItemData.item1_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item1_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[0].text) == float(ItemData.item1_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('fill the order form with the invalid data'):
        order_page.checkout_btn().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'
        order_page.input_fname().send_keys(OrderData.invalid_fname)
        order_page.input_lname().send_keys(OrderData.invalid_lname)
        order_page.input_zip().send_keys(OrderData.invalid_postal)

    with allure.step('enter the order confirmation page'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step2_url, 'Wrong URL'
        assert cart_page.cart_item_names()[0].text == ItemData.item1_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item1_desc, 'Different item description'
        assert cart_page.cart_item_prices()[0].text == ItemData.item1_price, 'Different item price'
        assert int(order_page.order_item_quantities()[0].text) == 1, 'Wrong items quantity in cart'

    with allure.step('check if the item information is correct'):
        items_sum = float(order_page.subtotal().text.lstrip('Item total: $'))
        assert items_sum == float(ItemData.item1_price.lstrip('$'))
        tax_sum = round(items_sum * OrderData.tax_rate, 2)
        assert tax_sum == float(order_page.tax().text.lstrip('Tax: $'))
        total_sum = float(order_page.total().text.lstrip('Total: $'))
        assert total_sum == round(items_sum + tax_sum, 2), 'Wrong total price'

    with allure.step('enter the order success page'):
        order_page.finish_btn().click()
        assert browser.current_url == URLs.checkout_complete_url and order_page.success_msg(), \
            'Wrong URL, success message is not shown'
        assert order_page.success_img().get_attribute('src') == OrderData.order_success_image, 'Wrong image'
        assert cart_page.cart_count_invisible(), 'Cart is not empty'
        assert len(cart_page.cart_item_names()) == 0, f'{len(cart_page.cart_item_names())} items in cart'

@allure.id('4.5')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order one item with empty fields')
@pytest.mark.negative
def test_item_order_empty_fields(browser, login, inv_page, cart_page, order_page):
    with allure.step('add items via the inventory page'):
        inv_page.inventory_add_items()[1].click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[0].text) == float(ItemData.item2_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('leave the order form empty'):
        order_page.checkout_btn().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'

    with allure.step('check if the error message is provided'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step1_url and order_page.error_msg1(), 'OK'
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

@allure.id('4.6')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order one item with an empty first name field')
@pytest.mark.negative
def test_item_order_empty_fname(browser, login, inv_page, cart_page, order_page):
    with allure.step('add items via the inventory page'):
        inv_page.inventory_add_items()[1].click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[0].text) == float(ItemData.item2_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('enter the last name and the postal code into the order form'):
        order_page.checkout_btn().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'
        order_page.input_lname().send_keys(OrderData.valid_lname)
        order_page.input_zip().send_keys(OrderData.valid_postal)

    with allure.step('check if the error message is provided'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step1_url and order_page.error_msg1(), 'OK'
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

@allure.id('4.7')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order one item with an empty last name field')
@pytest.mark.negative
def test_item_order_empty_lname(browser, login, inv_page, cart_page, order_page):
    with allure.step('add items via the inventory page'):
        inv_page.inventory_add_items()[1].click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[0].text) == float(ItemData.item2_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('enter the first name and the postal code into the order form'):
        order_page.checkout_btn().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'
        order_page.input_fname().send_keys(OrderData.valid_fname)
        order_page.input_zip().send_keys(OrderData.valid_postal)

    with allure.step('check if the error message is provided'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step1_url and order_page.error_msg2(), 'OK'
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

@allure.id('4.8')
@allure.epic('order page')
@allure.feature('order')
@allure.title('order one item with an empty postal code field')
@pytest.mark.negative
def test_item_order_empty_zip(browser, login, inv_page, cart_page, order_page):
    with allure.step('add items via the inventory page'):
        inv_page.inventory_add_items()[1].click()
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'

    with allure.step('enter the cart page'):
        cart_page.cart_btn().click()
        assert cart_page.cart_item_names()[0].text == ItemData.item2_name, 'Different item name'
        assert cart_page.cart_item_descs()[0].text == ItemData.item2_desc, 'Different item description'
        assert float(cart_page.cart_item_prices()[0].text) == float(ItemData.item2_price.lstrip('$')), \
            'Different item price'
        assert int(cart_page.cart_quantity().text) == 1, 'Wrong item quantity'

    with allure.step('enter the first name and the last name into the order form'):
        order_page.checkout_btn().click()
        assert browser.current_url == URLs.checkout_step1_url, 'Wrong URL'
        order_page.input_fname().send_keys(OrderData.valid_fname)
        order_page.input_lname().send_keys(OrderData.valid_lname)

    with allure.step('check if the error message is provided'):
        order_page.continue_btn().click()
        assert browser.current_url == URLs.checkout_step1_url and order_page.error_msg3(), 'OK'
        assert int(cart_page.cart_count().text) == 1, 'Wrong quantity'