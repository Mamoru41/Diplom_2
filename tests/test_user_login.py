import allure
import pytest
from helpers.api_client import ApiClient
from helpers.urls import Urls
from helpers.test_data import generate_random_email, TestData


class TestUserLogin:
    def setup_method(self):
        self.api_client = ApiClient()

    @allure.title("Успешный логин пользователя")
    def test_successful_login(self):
        """Логин под существующим пользователем"""
        with allure.step("Регистрация пользователя"):
            user_data = {
                "email": generate_random_email(),
                "password": TestData.VALID_PASSWORD,
                "name": TestData.VALID_NAME
            }
            self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Логин с корректными данными"):
            login_data = {
                "email": user_data["email"],
                "password": user_data["password"]
            }
            response = self.api_client.post(Urls.LOGIN, json=login_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.SUCCESS
            assert response.json()["success"] == True
            assert "accessToken" in response.json()
            assert "refreshToken" in response.json()

    @allure.title("Логин с неверным паролем")
    def test_login_with_wrong_password(self):
        """Логин с неверным паролем"""
        with allure.step("Регистрация пользователя"):
            user_data = {
                "email": generate_random_email(),
                "password": TestData.VALID_PASSWORD,
                "name": TestData.VALID_NAME
            }
            self.api_client.post(Urls.REGISTER, json=user_data)

        with allure.step("Логин с неверным паролем"):
            login_data = {
                "email": user_data["email"],
                "password": "wrong_password"
            }
            response = self.api_client.post(Urls.LOGIN, json=login_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.UNAUTHORIZED
            assert response.json()["success"] == False
            assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Логин с неверным email")
    def test_login_with_wrong_email(self):
        """Логин с неверным email"""
        with allure.step("Логин с несуществующим email"):
            login_data = {
                "email": "nonexistent_user@example.com",
                "password": TestData.VALID_PASSWORD
            }
            response = self.api_client.post(Urls.LOGIN, json=login_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == TestData.UNAUTHORIZED
            assert response.json()["success"] == False
            assert response.json()["message"] == "email or password are incorrect"