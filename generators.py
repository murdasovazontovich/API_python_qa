from faker import Faker
import random
from datetime import date

fake = Faker()

def generate_courier_payload():
    return {
        "login": fake.user_name(),
        "password": fake.password(length=10),
        "firstName": fake.first_name()
    }

def generate_courier_for_login():
    return {
        "login": fake.user_name(),
        "password": fake.password(length=10)}

def generate_order_payload():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 10),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": date.today().isoformat(),
        "comment": fake.sentence(),
        "color": [random.choice(["BLACK", "GREY"])]
    }