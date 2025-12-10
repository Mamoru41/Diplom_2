import allure
import pytest
from helpers.api_client import ApiClient
from helpers.urls import Urls
from helpers.test_data import generate_random_email, TestData


class TestUserRegistration:
    def setup_method(self):
        self.api_client = ApiClient()

    @allure.title("Успешная регистрация пользователя")
    def test_successful_registration(self):
        with allure.step("Подготовка данных пользователя"):
            user_data = {
                "email": generate_random_email(),
                "password": TestData.VALID_PASSWORD,
                "name": TestData.VALID_NAME
            }

        with allure.step("Отправка запроса регистрации"):
            response = self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.SUCCESS
            assert response.json()["success"] == True
            assert "accessToken" in response.json()

    @allure.title("Регистрация существующего пользователя")
    def test_register_existing_user(self):
        with allure.step("Регистрация первого пользователя"):
            user_data = {
                "email": generate_random_email(),
                "password": TestData.VALID_PASSWORD,
                "name": TestData.VALID_NAME
            }
            self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Попытка регистрации того же пользователя"):
            response = self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.FORBIDDEN
            assert response.json()["success"] == False
            assert response.json()["message"] == TestData.USER_EXISTS_MESSAGE

    @allure.title("Регистрация без обязательного поля email")
    def test_register_without_email(self):
        with allure.step("Подготовка данных без email"):
            user_data = {
                "password": TestData.VALID_PASSWORD,
                "name": TestData.VALID_NAME
            }

        with allure.step("Отправка запроса регистрации"):
            response = self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.FORBIDDEN
            assert response.json()["success"] == False
            assert response.json()["message"] == TestData.REQUIRED_FIELD_MESSAGE

    @allure.title("Регистрация без обязательного поля password")
    def test_register_without_password(self):
        with allure.step("Подготовка данных без password"):
            user_data = {
                "email": generate_random_email(),
                "name": TestData.VALID_NAME
            }

        with allure.step("Отправка запроса регистрации"):
            response = self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.FORBIDDEN
            assert response.json()["success"] == False
            assert response.json()["message"] == TestData.REQUIRED_FIELD_MESSAGE

    @allure.title("Регистрация без обязательного поля name")
    def test_register_without_name(self):
        with allure.step("Подготовка данных без name"):
            user_data = {
                "email": generate_random_email(),
                "password": TestData.VALID_PASSWORD
            }

        with allure.step("Отправка запроса регистрации"):
            response = self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.FORBIDDEN
            assert response.json()["success"] == False
            assert response.json()["message"] == TestData.REQUIRED_FIELD_MESSAGE