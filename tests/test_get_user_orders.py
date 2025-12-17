import allure
from api_shop import ApiRequests
from data import ResponseMessage


@allure.suite('Получение заказов пользователя')
class TestGetUserOrders:
    @allure.title('Получение списка заказов для авторизованного пользователя')
    @allure.description('''Направляем запрос на создание пользователя. Получив токен авторизации, направляем запрос на
                        создание заказа. После чего, с тем же токеном авторизации, направляем запрос на получение 
                        заказов пользователя. В ответе проверяем код и тело ответа. Созданного пользователя удаляем из 
                        базы после теста.''')
    def test_get_user_orders_with_sign_in(self, new_user, create_order):
        response = ApiRequests.get_user_orders(new_user.token)
        assert response.status_code == 200
        assert response.json()['success'] and len(response.json()['orders']) == 1

    @allure.title('Невозможно получить список заказов для неавторизованного пользователя')
    @allure.description('''Без токена авторизации, направляем запрос на получение заказов пользователя. 
                        В ответе проверяем код и тело ответа.''')
    def test_get_user_orders_without_sign_in(self):
        without_token = ''
        response = ApiRequests.get_user_orders(without_token)
        assert response.status_code == 401
        assert response.json() == ResponseMessage.YOU_SHOULD_BE_AUTHORISED