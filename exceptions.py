class BaseError(Exception):
    message = "Неожиданная ошибка"


class RequestError(BaseError):
    message = "Произошла ошибка обработки запроса"


class LogisticianError(BaseError):
    message = "Произошла ошибка при доставке"


class NotEnoughtSpace(LogisticianError):
    message = "Недостаточно места в магазине"


class NotEnoughtProduct(LogisticianError):
    message = "Недостаточно товара на складе"


class TooManyDifferentProducts(LogisticianError):
    message = "Слишком много разных товаров"


class InvalidRequest(RequestError):
    message = "Неправильный запрос. Попробуйте снова"


class InvalidStorageName(RequestError):
    message = "Выбран несуществующий склад"
