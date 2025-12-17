import requests
from data import Url


class ApiBodyBuilder:
    @staticmethod
    def build_user_body(email, password, name):
        user_body = {"email": email,
                     "password": password,
                     "name": name}
        return user_body

    @staticmethod
    def build_login_pass_body(email, password):
        login_pass_body = {"email": email,
                           "password": password}
        return login_pass_body

    @staticmethod
    def order_body(ingredients):
        order_body = {"ingredients": ingredients}
        return order_body


class ApiRequests:
    @staticmethod
    def create_user(body_user):
        return requests.post(f'{Url.STELLAR_BURGERS_URL}{Url.ENDPOINT_CREATING_USER}', json=body_user)

    @staticmethod
    def login_user(login_pass):
        return requests.post(f'{Url.STELLAR_BURGERS_URL}{Url.ENDPOINT_LOGIN}', data=login_pass)

    @staticmethod
    def changing_data_user(token, changing_body):
        return requests.patch(f'{Url.STELLAR_BURGERS_URL}{Url.ENDPOINT_USER}',
                              headers={'Authorization': token},
                              json=changing_body)

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{Url.STELLAR_BURGERS_URL}{Url.ENDPOINT_USER}',
                               headers={'Authorization': token})

    @staticmethod
    def create_order(token, order_body):
        return requests.post(f'{Url.STELLAR_BURGERS_URL}{Url.ENDPOINT_ORDER}',
                             headers={'Authorization': token},
                             json=order_body)

    @staticmethod
    def get_user_orders(token):
        return requests.get(f'{Url.STELLAR_BURGERS_URL}{Url.ENDPOINT_ORDER}',
                            headers={'Authorization': token})