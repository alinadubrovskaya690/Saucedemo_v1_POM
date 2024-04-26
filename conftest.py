import pytest
from selenium import webdriver

from pages.about_page import AboutPage
from pages.auth_page import LogPage, login
from pages.inventory_page import InventoryPage
from pages.items_page import ItemsPage
from pages.filter_page import FilterMod
from pages.sidebar_page import SidebarMod
from pages.cart_page import CartPage
from pages.order_page import OrderPage

from locators.urls import URLs


@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'normal'

    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--window-size=1200,800')
    chrome_options.add_argument('--incognito')
    #chrome_options.add_argument('--headless')

    browser = webdriver.Chrome(options=chrome_options)

    yield browser
    browser.quit()


@pytest.fixture()
def log_page(browser):
    log_page = LogPage(browser, URLs.auth_url)
    return log_page

@pytest.fixture()
def menu_page(browser):
    menu_page = SidebarMod(browser, login)
    return menu_page

@pytest.fixture()
def inv_page(browser):
    inv_page = InventoryPage(browser, URLs.inventory_url)
    return inv_page

@pytest.fixture()
def item_page(browser):
    item_page = ItemsPage(browser, login)
    return item_page

@pytest.fixture()
def filter_page(browser):
    filter_page = FilterMod(browser, login)
    return filter_page

@pytest.fixture()
def cart_page(browser):
    cart_page = CartPage(browser, URLs.cart_url)
    return cart_page

@pytest.fixture()
def order_page(browser):
    order_page = OrderPage(browser, URLs.checkout_complete_url)
    return order_page

@pytest.fixture()
def about_page(browser):
    about_page = AboutPage(browser, URLs.about_url)
    return about_page