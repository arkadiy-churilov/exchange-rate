import requests
from fake_useragent import UserAgent

usd = {
    'DT': '',
    'val_id': 'R01235',
    '_': '1685488301508'
}

eur = {
    'DT': '',
    'val_id': 'R01239',
    '_': '1685488908136'
}

def get_cours_crb(*args: dict, url='https://cbr.ru/cursonweek/') -> None:
    # Словарь кодов валют
    currencies = {
        'R01235': 'USD',
        'R01239': 'EUR',
        'R01375': 'CNY'
    }

    # Заголовки
    ua = UserAgent().random
    headers = {
        'user-agent': ua,
        'x-requested-with':	'XMLHttpRequest'
    }

    d = 0
    for param in args:

        # Запрос
        data = requests.get(url=url, headers=headers, params=param).json()[-1]

        # Выводит дату
        if d == 0:
            print(f'Дата: {".".join(data["data"][:10].split("-")[::-1])} г.')
            d += 1

        # Курс валют
        print(f'Курс {currencies[param["val_id"]]}: {data["curs"]:.2f} руб.')


get_cours_crb(usd, eur)

