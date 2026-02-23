import pytest
from generators import generate_courier_payload
from methods.register_courier import RegisterCourier
from methods.login_courier import LoginCourier
from methods.delete_courier import DeleteCourier


@pytest.fixture
def created_courier_and_delete():
    courier = generate_courier_payload()
    RegisterCourier.create_courier(courier)
    login_response = LoginCourier.login_courier({
        "login": courier["login"],
        "password": courier["password"]
    })
    courier_id = login_response.json()["id"]
    yield courier_id
    DeleteCourier.delete_courier(courier_id)


@pytest.fixture
def create_courier():
    courier = generate_courier_payload()
    RegisterCourier.create_courier(courier)
    login_response = LoginCourier.login_courier({
        "login": courier["login"],
        "password": courier["password"]
    })
    courier_id = login_response.json()["id"]
    yield courier_id
