user_str = input('''Введите элементы списка через любой односимвольный разделитель 
                 (разделителем будет выбран первый символ не являющийся числом или буквой): ''')
# разделитель по умолчанию
sep = ','
# проверим, может пользователь использует другой разделитель
for element in user_str:
  if not element.isalnum():
    sep = element
    print(f'Определен символ-разделитель: {sep}')
    break
# разберем строку по кусочкам и запишем в список
user_list = [int(i) for i in user_str.split(sep)]
# из списка сделаем множество, чтобы убрать повторяющиеся элементы
user_set = set(user_list)
# выводим результат
print(user_set)
