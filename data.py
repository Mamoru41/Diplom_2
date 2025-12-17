import random


class Url:
    STELLAR_BURGERS_URL = 'https://stellarburgers.nomoreparties.site'
    ENDPOINT_CREATING_USER = '/api/auth/register'
    ENDPOINT_LOGIN = '/api/auth/login'
    ENDPOINT_USER = '/api/auth/user'
    ENDPOINT_ORDER = '/api/orders'


class ResponseMessage:
    USER_ALREADY_EXISTS = {"success": False,
                           "message": "User already exists"}
    NOT_ENOUGH_DATA_FOR_CREATE = {"success": False,
                                  "message": "Email, password and name are required fields"}
    EMAIL_OR_PASSWORD_ARE_INCORRECT = {"success": False,
                                       "message": "email or password are incorrect"}
    YOU_SHOULD_BE_AUTHORISED = {"success": False,
                                "message": "You should be authorised"}
    INGREDIENTS_MUST_BE_PROVIDED = {"success": False,
                                    "message": "Ingredient ids must be provided"}
    INTERNAL_SERVER_ERROR = 'Internal Server Error'


class Ingredients:
    BUNS = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6c']
    INGREDIENTS = ['61c0c5a71d1f82001bdaaa6f',
                   '61c0c5a71d1f82001bdaaa70',
                   '61c0c5a71d1f82001bdaaa71',
                   '61c0c5a71d1f82001bdaaa72',
                   '61c0c5a71d1f82001bdaaa6e',
                   '61c0c5a71d1f82001bdaaa73',
                   '61c0c5a71d1f82001bdaaa74',
                   '61c0c5a71d1f82001bdaaa75',
                   '61c0c5a71d1f82001bdaaa76',
                   '61c0c5a71d1f82001bdaaa77',
                   '61c0c5a71d1f82001bdaaa78',
                   '61c0c5a71d1f82001bdaaa79',
                   '61c0c5a71d1f82001bdaaa7a']
    BUN = random.choice(BUNS)
    INGREDIENT = random.choice(INGREDIENTS)