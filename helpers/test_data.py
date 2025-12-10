import random
import string


class TestData:
    # Пользователи
    VALID_PASSWORD = "password123"
    VALID_NAME = "Test User"

    # Ожидаемые статус-коды
    SUCCESS = 200
    FORBIDDEN = 403
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    INTERNAL_ERROR = 500

    # Сообщения об ошибках
    USER_EXISTS_MESSAGE = "User already exists"
    REQUIRED_FIELD_MESSAGE = "Email, password and name are required fields"


def generate_random_email():
    """Генерирует случайный email для тестов"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"test_user_{random_string}@example.com"