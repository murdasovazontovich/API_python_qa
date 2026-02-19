# API Tests for Yandex Samokat

Набор автотестов API сервиса «Яндекс Самокат» на `pytest` с отчетами в `Allure`.

## Что проверяется

Тестовые сценарии покрывают основные ручки:

- регистрация курьера
- логин курьера
- удаление курьера
- создание заказа
- получение списка заказов

Базовый URL API: `https://qa-scooter.praktikum-services.ru`

## Стек
- Python 3.9+
- pytest
- requests
- allure-pytest
- faker

## Структура проекта
.
├── curl.py                # URL и эндпоинты API
├── data.py                # тестовые константы
├── generators.py          # генераторы тестовых данных
├── methods/               # методы для работы с API
├── tests/                 # тесты`