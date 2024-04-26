# **Page Object Module**

**Autotests for Sauce Labs site**

**Объект тестирования:** интернет-магазин saucedemo.com v1
**Site URL:** https://www.saucedemo.com/v1/index.html
**Стек:** Python, Pytest, Selenium


**Функционал для тестирования**

**Авторизация:**
1. Авторизация с использованием валидных данных (standard_user, secret_sauce)
2. Авторизация с использованием валидных данных (locked_out_user, secret_sauce)
3. Авторизация с использованием валидных данных (problem_user, secret_sauce)
4. Авторизация с использованием валидных данных (performance_glitch_user, secret_sauce)
5. Авторизация с использованием невалидных данных
6. Авторизация с использованием пустых полей ввода
7. Авторизация с пустым полем Username
8. Авторизация с пустым полем Password

**Корзина:**
1. Добавление и удаление товаров через каталог
2. Добавление и удаление товаров через страницу товара
3. Добавление товаров через страницу товара и его удаление через страницу корзины

**Страница товара:**
1. Переход на страницу товара после клика на картинку
2. Переход на страницу товара после клика на название

**Фильтр:**
1. Проверка работы кнопок фильтра:
    1.1. По названию (A to Z, Z to A)
    1.2. По цене (low to high, high to low)

**Сайдбар:**
1. Переход на страницу каталога (All Items)
2. Выход из системы (Logout)
3. Переход на страницу "About" (About) 
4. Сброс заказа в корзине (Reset App State)

**Заказ:**
1. Заказ одного товара используя валидные данные
2. Заказ нескольких товаров используя валидные данные
3. Заказ одного товара с пустой формой оформления заказа
4. Заказ одного товара с пустым полем ввода имени заказчика
5. Заказ одного товара с пустым полем ввода фамилии заказчика
6. Заказ одного товара с пустым полем ввода почтового индекса заказчика
7. Заказ пустой корзины используя валидные данные