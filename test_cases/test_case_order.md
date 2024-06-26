# **test-case 1. Оформление одного заказа используя валидные данные**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Выбрать товар из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Нажать на иконку корзины (переход на страницу корзины: https://www.saucedemo.com/v1/cart.html)
3. Нажать на кнопку "CHECKOUT" (переход на страницу формы оформления заказа: 
https://www.saucedemo.com/v1/checkout-step-one.html)
4. Заполнить форму оформления заказа валидными данными
5. Нажать на кнопку "CONTINUE" (переход на страницу подтверждения заказа: 
https://www.saucedemo.com/v1/checkout-step-two.html)
6. Нажать на кнопку "FINISH"

**Ожидаемый результат:** Осуществляется переход на страницу сообщения об успешном заказе: 
https://www.saucedemo.com/v1/checkout-complete.html. Оформление заказа прошло успешно


# **test-case 2. Оформление нескольких заказов используя валидные данные**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Выбрать товары из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Нажать на иконку корзины (переход на страницу корзины: https://www.saucedemo.com/v1/cart.html)
3. Нажать на кнопку "CHECKOUT" (переход на страницу формы оформления заказа: 
https://www.saucedemo.com/v1/checkout-step-one.html)
4. Заполнить форму оформления заказа валидными данными
5. Нажать на кнопку "CONTINUE" (переход на страницу подтверждения заказа: 
https://www.saucedemo.com/v1/checkout-step-two.html)
6. Нажать на кнопку "FINISH"

**Ожидаемый результат:** Осуществляется переход на страницу сообщения об успешном заказе: 
https://www.saucedemo.com/v1/checkout-complete.html. Оформление заказа прошло успешно
 

# **test-case 3. Заказ одного товара используя пустые поля ввода**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**

1. Выбрать товар из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Нажать на иконку корзины (переход на страницу корзины: https://www.saucedemo.com/v1/cart.html)
3. Нажать на кнопку "CHECKOUT" (переход на страницу формы оформления заказа: 
https://www.saucedemo.com/v1/checkout-step-one.html)
4. Оставить форму оформления заказа пустой и нажать на кнопку "CONTINUE"

**Ожидаемый результат:** Появляется сообщение об ошибке. Пользователь остаётся на странице формы оформления заказа


# **test-case 4. Заказ пустой корзины используя валидные данные**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**
1. Нажать на иконку корзины

**Ожидаемый результат:** Осуществляется переход на страницу корзины: https://www.saucedemo.com/v1/cart.html. 
Кнопка "CHECKOUT" недоступна для использования


# **test-case 5. Заказ одного товара с пустым полем ввода имени заказчика**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**

1. Выбрать товар из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Нажать на иконку корзины (переход на страницу корзины: https://www.saucedemo.com/v1/cart.html)
3. Нажать на кнопку "CHECKOUT" (переход на страницу формы оформления заказа: 
https://www.saucedemo.com/v1/checkout-step-one.html)
4. Заполнить все поля формы оформления заказа, кроме поля ввода имени заказчика
5. Нажать на кнопку "CONTINUE"

**Ожидаемый результат:** Появляется сообщение об ошибке. Пользователь остаётся на странице формы оформления заказа


# **test-case 6. Заказ одного товара с пустым полем ввода фамилии заказчика**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**

1. Выбрать товар из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Нажать на иконку корзины (переход на страницу корзины: https://www.saucedemo.com/v1/cart.html)
3. Нажать на кнопку "CHECKOUT" (переход на страницу формы оформления заказа: 
https://www.saucedemo.com/v1/checkout-step-one.html)
4. Заполнить все поля формы оформления заказа, кроме поля ввода фамилии заказчика
5. Нажать на кнопку "CONTINUE"

**Ожидаемый результат:** Появляется сообщение об ошибке. Пользователь остаётся на странице формы оформления заказа


# **test-case 7. Заказ одного товара с пустым полем ввода почтового индекса заказчика**

**Предусловие:** Пользователь авторизован. Отображается страница каталога товаров 
(https://www.saucedemo.com/v1/inventory.html)

**Шаги воспроизведения:**

1. Выбрать товар из каталога нажав на кнопку "ADD TO CART" на странице каталога товаров
2. Нажать на иконку корзины (переход на страницу корзины: https://www.saucedemo.com/v1/cart.html)
3. Нажать на кнопку "CHECKOUT" (переход на страницу формы оформления заказа: 
https://www.saucedemo.com/v1/checkout-step-one.html)
4. Заполнить все поля формы оформления заказа, кроме поля ввода почтового индекса заказчика
5. Нажать на кнопку "CONTINUE"

**Ожидаемый результат:** Появляется сообщение об ошибке. Пользователь остаётся на странице формы оформления заказа