import allure
from methods.get_order import GetOrder


class TestGetOrder:
    @allure.title("Получить заказ")
    def test_get_order(self):
        response = GetOrder.get_order(self)

        assert response.status_code == 200
        assert 'orders' in response.json()