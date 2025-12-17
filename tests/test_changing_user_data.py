import pytest
import allure
from api_shop import ApiRequests, ApiBodyBuilder
from data import ResponseMessage


@allure.suite('Изменение данных пользователя')
class TestChangingUserData:
    @allure.title('Успешное изменение данных авторизованного пользователя')
    @allure.description('''Направляем запрос на создание пользователя. Получив токен авторизации,
                        с помощию параметризации проверяем возможность изменения данных пользователя в полях:
                        'email', 'password', 'name'. В ответе проверяем код и тело ответа.
                         Созданного пользователя удаляем из базы после теста.''')
    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_changing_user_data_with_sign_in(self, user_data, new_user, index):
        changed_data = f'{user_data[index]}f'
        user_data[index] = changed_data
        body = ApiBodyBuilder.build_user_body(user_data[0], user_data[1], user_data[2])
        response = ApiRequests.changing_data_user(new_user.token, body)
        assert response.status_code == 200
        assert response.json()['success']

    @allure.title('Невозможно изменить данные пользователя без авторизации')
    @allure.description('''Создаем пользователя. С помощию параметризации проверяем возможность изменения данных 
                        пользователя в полях: 'email', 'password', 'name' без передачи токена авторизации. 
                        В ответе проверяем код и тело ответа. Созданного пользователя удаляем из базы после теста. ''')
    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_changing_user_data_without_sign_in(self, user_data, new_user, index):
        user_data_copy = user_data.copy()
        changed_data = f'{user_data_copy[index]}f'
        user_data_copy[index] = changed_data
        body = ApiBodyBuilder.build_user_body(user_data_copy[0], user_data_copy[1], user_data_copy[2])
        without_token = ''
        response = ApiRequests.changing_data_user(without_token, body)
        assert response.status_code == 401
        assert response.json() == ResponseMessage.YOU_SHOULD_BE_AUTHORISED