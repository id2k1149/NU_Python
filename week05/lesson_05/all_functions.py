# модуль где лежат все функции
import random


def get_random_person():
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушнин': '26.06.1799',
                     'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895',
                     'Владимир Семенович Высоцкий': '25.01.1938',
                     'Виктор Робертович Цой': '21.06.1962',
                     'Константин Эдуардович Циолковский': '17.09.1857',
                     'Сергей Павлович Королев': '12.01.1907',
                     'Валентин Петрович Глушко': '20.08.1908',
                     'Андрей Николаевич Туполев': '29.10.1888',
                     'Юрий Алексеевич Гагарин': '09.03.1934'}

    name, date = random.choice(list(FAMOUS_PEOPLE.items()))
    return name, date


def get_person_and_question():
    name, date = get_random_person()

    answer = input(f'Когда родился {name} ')

    # Если введенный год совпадает с правильным
    if answer == date:
        print('Верно')
    else:
        print('Неверно')


print('__name__ = ', __name__)
print(get_person_and_question())
