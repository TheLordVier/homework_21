from entity.logistician import Logistician
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import LogisticianError, RequestError

store = Store(items={})
shop = Shop(items={})

store.items = {
    "печенька": 3,
    "собачка": 2,
    "мяч": 1,
    "хлеб": 2,
    "коробки": 3,
}

shop.items = {
    "печенька": 2,
    "собачка": 1,
    "мяч": 1,
    "хлеб": 2,
    "коробки": 1
}

storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    print("\nДобрый день!\n")

    while True:
        # Вывод содержимого складов
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].items}')

        # Запрос ввода от пользователя
        user_input = input(
            "Введите ваш запрос в формате 'Доставить 3 коробки из склад в магазин'\n"
            "Введите 'stop' или 'стоп', если захотите закончить:\n"
        )
        if user_input in ("stop", "стоп"):
            break

        # Валидация ввода пользователя
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        # Выполнение доставки
        logistician = Logistician(
            request=request,
            storages=storages,
        )
        try:
            logistician.move()
        except LogisticianError as error:
            print(error.message)


if __name__ == '__main__':
    main()
