import pytest
import allure
from methods.create_order import CreateOrder

class TestCreateOrder:
    @allure.title("Создание заказа с разными данными")
    @pytest.mark.parametrize("payload", [{
    "firstName": "sdkldk",
    "lastName": "Potter",
    "address": "Аэропорт 1",
    "metroStation": 5,
    "phone": "+7 800 355 35 35",
    "rentTime": 3,
    "deliveryDate": "2026-03-05",
    "comment": "Дайте 2",
    "color": [
        "BLACK"
    ]
},
{
    "firstName": "sdkldk",
    "lastName": "Дамблдор",
    "address": "Кремль 2",
    "metroStation": 1,
    "phone": "+7 800 355 35 35",
    "rentTime": 10,
    "deliveryDate": "2026-04-01",
    "comment": "Все самокаты",
    "color": [
        "GREY"
    ]
}, 
{
    "firstName": "sdkldk",
    "lastName": "Кхалиси",
    "address": "Красная гавань 1",
    "metroStation": 10,
    "phone": "+7 800 355 35 35",
    "rentTime": 1,
    "deliveryDate": "2026-06-06",
    "comment": "Дракарис",
    "color": [
        "BLACK","GREY"
    ]
}, 
{
    "firstName": "sdkldk",
    "lastName": "Сноу",
    "address": "Черный замок 4",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 2,
    "deliveryDate": "2026-12-10",
    "comment": "Зима близко"
}])
    def test_create_order(self, payload):
        response = CreateOrder.create_order(payload=payload)
        body = response.json()

        assert response.status_code == 201
        assert "track" in body 
        assert body["track"] > 0