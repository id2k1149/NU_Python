"""
Написать программу используя условные операторы:
- Спросить у пользователя год рождения А.С Пушкина
- Если пользователь ввел верный год вывести 'Верно'
- Если пользователь ошибся вывести 'Неверно'
"""
born_year = input('Напишите год рождения А.С.Пушкина. ')
if int(born_year) == 1799:
    print('Верно')
else:
    print('Неверно')
