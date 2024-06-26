# **test-case 1. Переход на страницу товара после клика на название**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на название товара

**Ожидаемый результат:** Осуществляется переход на страницу товара 


# **test-case 2. Переход на страницу товара после клика на картинку**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на картинку товара

**Ожидаемый результат:** Осуществляется переход на страницу товара


# **test-case 3. Добавление и удаление товаров через каталог**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Выбрать товар из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Убрать товар из корзины нажав на кнопку "REMOVE" на странице каталога товаров

**Ожидаемый результат:** Товар удален из корзины. Счетчик товаров в корзине исчезает


# **test-case 4. Добавление и удаление товаров через страницу товара**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на название товара (переход на страницу товара)
2. Нажать на кнопку "ADD TO CART" на странице товара
3. Нажать на кнопку "REMOVE" на странице товара

**Ожидаемый результат:** Товар удален из корзины. Счетчик товаров в корзине исчезает


# **test-case 5. Добавление товаров через страницу товара и его удаление через страницу корзины**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на название товара (переход на страницу товара)
2. Нажать на кнопку "ADD TO CART" на странице товара
3. Нажать на иконку корзины (переход на страницу корзины: https://www.saucedemo.com/v1/cart.html)
4. Нажать на кнопку "REMOVE" на странице корзины

**Ожидаемый результат:** Товар удален из корзины. Счетчик товаров в корзине исчезает