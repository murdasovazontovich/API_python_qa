import pytest
import allure
from data import COURIER_LOGIN
from generators import generate_courier_for_login
from methods.login_courier import LoginCourier


class TestLoginCourier:
    @allure.title("Залогиниться курьеру")
    def test_login_courier(self):
        response = LoginCourier.login_courier(payload=COURIER_LOGIN)
        body = response.json()

        assert response.status_code == 200
        assert "id" in body
        assert body["id"] > 0

    @allure.title("Неудачный логин без обязательного поля")
    @pytest.mark.parametrize("payload", [{"password": "12345"},
                                          {"login": "piojh"},])
    def test_login_missing_required_field(self,payload):
        response = LoginCourier.login_courier(payload=payload)

        assert response.status_code == 400
        assert response.json() == {"message":  "Недостаточно данных для входа"}

    @allure.title("Залогиниться курьеру, которого не существует")
    def test_login_nonexistent_courier(self):
        payload = generate_courier_for_login()
        response = LoginCourier.login_courier(payload)

        assert response.status_code == 404
        assert response.json() == {"message": "Учетная запись не найдена"}