import pytest
import allure
from api_shop import ApiRequests, ApiBodyBuilder
from data import Ingredients, ResponseMessage


@allure.suite('Создание заказа')
class TestCreateOrder:
    @allure.title('Cоздание заказа c ингредиентами для авторизованного пользователя')
    @allure.description('''Направляем запрос на создание пользователя. Получив токен авторизации, 
                        направляем запрос на создание заказа с полным набором валидных данных (хэш ингредиентов).
                        В ответе проверяем код и тело ответа. Созданного пользователя удаляем из базы после теста.''')
    @pytest.mark.parametrize('ingredients', [[Ingredients.BUN],
                                             [Ingredients.BUN, Ingredients.INGREDIENT],
                                             [Ingredients.BUN, Ingredients.INGREDIENT, Ingredients.INGREDIENT]])
    def test_create_order_with_sign_in(self, new_user, ingredients):
        order_body = ApiBodyBuilder.order_body(ingredients)
        response = ApiRequests.create_order(new_user.token, order_body)
        assert response.status_code == 200
        assert response.json()['success']

    @allure.title('Cоздание заказа c ингредиентами для неавторизованного пользователя')
    @allure.description(''' Направляем запрос на создание заказа с полным набором валидных данных
                        (хэш ингредиентов) без передачи токена авторизации. В ответе проверяем код и тело ответа''')
    @pytest.mark.parametrize('ingredients', [[Ingredients.BUN],
                                             [Ingredients.BUN, Ingredients.INGREDIENT],
                                             [Ingredients.BUN, Ingredients.INGREDIENT, Ingredients.INGREDIENT]])
    def test_create_order_without_sign_in(self, ingredients):
        order_body = ApiBodyBuilder.order_body(ingredients)
        without_token = ''
        response = ApiRequests.create_order(without_token, order_body)
        assert response.status_code == 200
        assert response.json()['success']

    @allure.title('Создание заказа без ингрeдиентов')
    @allure.description('''Направляем запрос на создание пользователя. Получив токен авторизации, направляем запрос на 
                        создание заказа без ингредиентов. В ответе проверяем код и тело ответа. Cозданного 
                        пользователя удаляем из базы после теста.''')
    def test_create_order_without_ingredients(self, new_user):
        order_body = ApiBodyBuilder.order_body([])
        response = ApiRequests.create_order(new_user.token, order_body)
        assert response.status_code == 400
        assert response.json() == ResponseMessage.INGREDIENTS_MUST_BE_PROVIDED

    @allure.title('Создание заказа с неправильным id ингрeдиента')
    @allure.description('''Направляем запрос на создание пользователя. Получив токен авторизации, направляем запрос на 
                            создание заказа с невалидными данными (хэш ингредиента). В ответе проверяем код и тело 
                            ответа. Cозданного пользователя удаляем из базы после теста.''')
    def test_create_order_error_id_ingredient(self, new_user):
        order_body = ApiBodyBuilder.order_body([f'{Ingredients.INGREDIENT}f'])
        response = ApiRequests.create_order(new_user.token, order_body)
        assert response.status_code == 500
        assert ResponseMessage.INTERNAL_SERVER_ERROR in response.text
