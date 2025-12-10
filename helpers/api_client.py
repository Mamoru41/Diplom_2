import allure
import requests


class ApiClient:
    def __init__(self):
        self.session = requests.Session()

    @allure.step("POST запрос на {endpoint}")
    def post(self, endpoint, json=None, headers=None):
        return self.session.post(endpoint, json=json, headers=headers)

    @allure.step("GET запрос на {endpoint}")
    def get(self, endpoint, headers=None):
        return self.session.get(endpoint, headers=headers)