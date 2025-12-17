import pytest
import allure
from fake_data import FakeData
from api_shop import ApiRequests, ApiBodyBuilder
from collections import namedtuple
from data import Ingredients


@allure.step('Получаем данные для создания пользователя. Финализатор с удалением пользователя')
@pytest.fixture
def user_data():
    email = FakeData.email()
    password = FakeData.password()
    name = FakeData.name()
    array = [email, password, name]
    yield array
    login_pass_body = ApiBodyBuilder.build_login_pass_body(array[0], array[1])
    response = ApiRequests.login_user(login_pass_body)
    token = response.json()['accessToken']
    ApiRequests.delete_user(token)


@allure.step('Создаем пользователя и передаем в тесты токен авторизации')
@pytest.fixture
def new_user(user_data):
    user_body = ApiBodyBuilder.build_user_body(user_data[0], user_data[1], user_data[2])
    response = ApiRequests.create_user(user_body)
    token = response.json()['accessToken']
    UserToken = namedtuple('UserToken', ['token'])
    return UserToken(token)


@allure.step('Создаем заказ')
@pytest.fixture
def create_order(new_user):
    order_body = ApiBodyBuilder.order_body([Ingredients.INGREDIENT])
    return ApiRequests.create_order(new_user.token, order_body)