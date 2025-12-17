import allure
import pytest
from api_shop import ApiRequests, ApiBodyBuilder
from data import ResponseMessage


@allure.suite('Авторизация пользователя')
class TestLoginUser:
    @allure.title('Успешная авторизация зарегистрированного пользователя при заполнении всех обязательных полей')
    @allure.description('''Направляем запрос на создание пользователя пользователя с валидными данными,
                        далее направляем запрос на авторизацию этого пользователя. В ответе проверяем код и тело 
                        ответа. Созданного пользователя удаляем из базы после теста.''')
    def test_login_user(self, user_data, new_user):
        body = ApiBodyBuilder.build_login_pass_body(user_data[0], user_data[1])
        response = ApiRequests.login_user(body)
        assert response.status_code == 200
        assert response.json()['success']

    @allure.title('Нельзя авторизоваться зарегистрированному пользователю c неправильно заполненным обязательным полем')
    @allure.description('''Направляем запрос на создание пользователя с валидными данными,
                        далее c помощью параметризации направляем запрос на авторизацию этого пользователя с 
                        ошибочными данными в одном из полей для авторизации (email и password). 
                        В ответе проверяем код и тело ответа. Созданного пользователя удаляем из базы после теста.''')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_login_user_with_error_in_field(self, field, user_data, new_user):
        body = ApiBodyBuilder.build_login_pass_body(user_data[0], user_data[1])
        error_data = f'{body[field]}f'
        body[field] = error_data
        response = ApiRequests.login_user(body)
        assert response.status_code == 401
        assert response.json() == ResponseMessage.EMAIL_OR_PASSWORD_ARE_INCORRECT