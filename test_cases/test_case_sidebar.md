# **test-case 1. Переход на страницу каталога товаров**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на название товара (переход на страницу товара)
2. Нажать на иконку сайдбара
3. Нажать на кнопку "All Items"

**Ожидаемый результат:** Осуществляется переход на страницу каталога товаров: 
https://www.saucedemo.com/v1/inventory.html


# **test-case 2. Переход на страницу "About"**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на иконку сайдбара
2. Нажать на кнопку "About" 

**Ожидаемый результат:** Осуществляется переход на страницу "About": https://saucelabs.com/


# **test-case 3. Выход из системы**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на иконку сайдбара
2. Нажать на кнопку "Logout"

**Ожидаемый результат:** Осуществляется переход на страницу авторизации пользователя: 
https://www.saucedemo.com/v1/index.html


# **test-case 4. Сброс заказа в корзине**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Выбрать товары из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Нажать на иконку сайдбара
3. Нажать на кнопку "Reset App State"

**Ожидаемый результат:** Товары удалены из корзины. Счетчик товаров в корзине исчезает