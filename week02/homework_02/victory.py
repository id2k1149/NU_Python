"""
Выбрать минимум 5 известных людей и узнать их год рождения.
Программа должна по очереди спрашивать у пользователя год рождения знаменитости.
После того как пользователь ввел все ответы, программа считает и выводит на экран:
- количество правильных ответов
- количество ошибок
- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
- процент неправильных ответов
После вывода информации программа спрашивает пользователя хочет ли он начать игру сначала,
если да - то повторяем все сначала, если ответ нет - выходим из программы
- В программе с помощью комментариев написать подсказки - правильные ответы для каждой знаменитости
"""

user_choice = 'Y'

while user_choice == 'Y':
    true_answer = 0
    born_year = input('В каком году родился Ньютон? ')
    # Ньютон 1643
    if born_year == '1643':
        true_answer += 1
    born_year = input('В каком году родился Колумб? ')
    # Колумб 1451
    if born_year == '1451':
        true_answer += 1
    born_year = input('В каком году родился Энштейн? ')
    # Энштейн 1879
    if born_year == '1879':
        true_answer += 1
    born_year = input('В каком году родился Галилей? ')
    # Галилей 1564
    if born_year == '1564':
        true_answer += 1
    born_year = input('В каком году родился Дарвин? ')
    # Дарвин 1809
    if born_year == '1809':
        true_answer += 1
    print('количество правильных ответов =', true_answer)
    print('количество ошибок =', 5 - true_answer)
    print('процент правильных ответов =', true_answer * 20, '%')
    print('процент неправильных ответов = ', 100 - true_answer * 20, '%')
    user_choice = input('Если хотите повторить, нажмите  Y')
    if user_choice != 'Y':
        break
