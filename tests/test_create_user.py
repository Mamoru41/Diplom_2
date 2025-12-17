import pytest
import allure
from api_shop import ApiRequests, ApiBodyBuilder
from data import ResponseMessage
from fake_data import FakeData


@allure.suite('Проверка создания пользователя.')
class TestCreatingUser:
    @allure.title('Успешное создание пользователя при заполнении всех полей')
    @allure.description('''Направляем запрос на создание пользователя с полным набором валидных данных. В ответе 
                        проверяем код и тело ответа. Созданного пользователя удаляем из базы после теста.''')
    def test_creating_new_user(self, user_data):
        user_body = ApiBodyBuilder.build_user_body(user_data[0], user_data[1], user_data[2])
        response = ApiRequests.create_user(user_body)
        assert response.status_code == 200
        assert response.json()['success']

    @allure.title('Невозможно создать пользователя, который уже зарегистрирован')
    @allure.description('''Поочередно направляем два запроса на создание пользователя с одинаковым набором валидных 
                        данных. В ответе проверяем код и тело ответа. Созданного пользователя удаляем из базы
                        после теста.''')
    def test_creating_same_user(self, user_data):
        user_body = ApiBodyBuilder.build_user_body(user_data[0], user_data[1], user_data[2])
        ApiRequests.create_user(user_body)
        response = ApiRequests.create_user(user_body)
        assert response.status_code == 403
        assert response.json() == ResponseMessage.USER_ALREADY_EXISTS

    @allure.title('Нельзя создать пользователя, не заполнив одно из обязательных полей')
    @allure.description('''Направляем запрос на создание пользователя с неполным набором валидных данных.
                        Используя параметризацию проверяем результат при отправке запроса без заполнения каждого из
                        обязательных полей. В ответе проверяем код и тело ответа.''')
    @pytest.mark.parametrize('email, password, name', [['', FakeData.password(), FakeData.name()],
                                                       [FakeData.email(), '', FakeData.name()],
                                                       [FakeData.email(), FakeData.password(), '']])
    def test_creating_user_without_required_field(self, email, password, name):
        body_user = ApiBodyBuilder.build_user_body(email, password, name)
        response = ApiRequests.create_user(body_user)
        assert response.status_code == 403
        assert response.json() == ResponseMessage.NOT_ENOUGH_DATA_FOR_CREATE