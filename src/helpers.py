from faker import Faker
import time

fake = Faker()

def get_sign_up_data():
    name = fake.name()
    email = fake.email()
    password = fake.password()
    return name, email, password