import pytest
import allure
from methods.create_order import CreateOrder
from data import ORDER_PAYLOADS

class TestCreateOrder:
    @allure.title("Создание заказа с разными данными")
    @pytest.mark.parametrize("payload", ORDER_PAYLOADS)
    def test_create_order(self, payload):
        response = CreateOrder.create_order(payload=payload)
        body = response.json()

        assert response.status_code == 201
        assert "track" in body 
        assert body["track"] > 0