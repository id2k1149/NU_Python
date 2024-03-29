"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""


def rounding_sum(value):
    kopeyka = abs(value * 100)
    ruble = int(kopeyka // 100)
    kopeyka = abs(value) - ruble
    kopeyka = int(float('{0:.10}'.format(kopeyka)) * 100)
    if kopeyka == 0:
        kopeyka = str('00')
    elif kopeyka < 10:
        kopeyka = '0' + str(kopeyka)
    else:
        kopeyka = str(kopeyka)
    ruble_and_kopeyka = dict([(1, ruble), (2, kopeyka)])
    return ruble_and_kopeyka


def refill_account(old_balance):
    add_value = float(input('Введите сумму пополения: '))
    round_add_value = rounding_sum(add_value)
    print(f'На Ваш счет будет добавлено {round_add_value[1]} руб {round_add_value[2]} коп')
    print('-------------------')
    if int(round_add_value[2]) / 100 > 100:
        kopeyka = (int(round_add_value[2]) - 100) / 100
        ruble = round_add_value[1] + 1
        old_balance += ruble + kopeyka
        return old_balance
    return old_balance + round_add_value[1] + int(round_add_value[2]) / 100


def purchase(old_balance):
    price = float(input('Введите сумму покупки: '))
    round_price = rounding_sum(price)
    print(f'Цена покупки {round_price[1]} руб {round_price[2]} коп')
    if old_balance < price:
        print('На покупку не хватает денег')
        return old_balance
    else:
        expence_name = input('Введите название покупки, например (еда)')
        expence_history = dict([(1, ruble), (2, kopeyka)])



balance = float(0)
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print('-------------------')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        balance = refill_account(balance)
        round_value = rounding_sum(balance)
        print(f'У Вас на счете {round_value[1]} руб {round_value[2]} коп')
        print('-------------------')
    elif choice == '2':
        balance = purchase(balance)
        round_value = rounding_sum(balance)
        print(f'У Вас на счете {round_value[1]} руб {round_value[2]} коп')
        print('-------------------')
    elif choice == '3':
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')


