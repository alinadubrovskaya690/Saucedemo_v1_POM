import pytest
import allure
from pages.auth_page import login


@allure.id('3.1')
@allure.epic('filter page')
@allure.feature('filter')
@allure.title('az button')
@pytest.mark.positive
def test_az(browser, login, inv_page, filter_page):
    with allure.step('sort the items by name before clicking the button'):
        items_before_az = inv_page.inventory_names()
        before_az = []
        for item in items_before_az:
            before_az.append(item.text)

    before_az.sort(reverse=False)
    print(f'\n{before_az}')

    with allure.step('sort the items by name after clicking the button'):
        filter_page.filter_az().click()

    with allure.step('check if the button works properly'):
        items_after_az = inv_page.inventory_names()
        after_az = []
        for item in items_after_az:
            after_az.append(item.text)
        print(f'\n{after_az}')

        assert before_az == after_az, 'Filter A to Z does\'t work properly'

    inv_page.refresh()

@allure.id('3.2')
@allure.epic('filter page')
@allure.feature('filter')
@allure.title('za button')
@pytest.mark.positive
def test_za(browser, login, inv_page, filter_page):
    with allure.step('sort the items by name before clicking the button'):
        items_before_za = inv_page.inventory_names()
        before_za = []
        for item in items_before_za:
            before_za.append(item.text)

    before_za.sort(reverse=True)
    print(f'\n{before_za}')

    with allure.step('check if the button works properly'):
        filter_page.filter_za().click()

    with allure.step('sort the items by name after clicking the button'):
        items_after_za = inv_page.inventory_names()
        after_za = []
        for item in items_after_za:
            after_za.append(item.text)
        print(f'\n{after_za}')

        assert before_za == after_za, 'Filter Z to A does\'t work properly'

    inv_page.refresh()

@allure.id('3.3')
@allure.epic('filter page')
@allure.feature('filter')
@allure.title('low to high button')
@pytest.mark.positive
def test_lohi(browser, login, inv_page, filter_page):
    with allure.step('sort the items by price before clicking the button'):
        prices_before_lohi = inv_page.inventory_prices()
        before_lohi = []
        for item in prices_before_lohi:
            before_lohi.append(float(item.text.lstrip('$')))

    before_lohi.sort(reverse=False)
    print(f'\n{before_lohi}')

    with allure.step('check if the button works properly'):
        filter_page.filter_lohi().click()

    with allure.step('sort the items by price after clicking the button'):
        prices_after_lohi = inv_page.inventory_prices()
        after_lohi = []
        for item in prices_after_lohi:
            after_lohi.append(float(item.text.lstrip('$')))
        print(f'\n{after_lohi}')

        assert before_lohi == after_lohi, 'Filter Low to High does\'t work properly'

    inv_page.refresh()

@allure.id('3.4')
@allure.epic('filter page')
@allure.feature('filter')
@allure.title('high to low button')
@pytest.mark.positive
def test_hilo(browser, login, inv_page, filter_page):
    with allure.step('sort the items by price before clicking the button'):
        prices_before_hilo = inv_page.inventory_prices()
        before_hilo = []
        for item in prices_before_hilo:
            before_hilo.append(float(item.text.lstrip('$')))

    before_hilo.sort(reverse=True)
    print(f'\n{before_hilo}')

    with allure.step('check if the button works properly'):
        filter_page.filter_hilo().click()

    with allure.step('sort the items by price after clicking the button'):
        prices_after_hilo = inv_page.inventory_prices()
        after_hilo = []
        for item in prices_after_hilo:
            after_hilo.append(float(item.text.lstrip('$')))
        print(f'\n{after_hilo}')

        assert before_hilo == after_hilo, 'Filter Low to High does\'t work properly'

    inv_page.refresh()