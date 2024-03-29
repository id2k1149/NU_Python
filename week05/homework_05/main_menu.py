# Main menu
import os
import shutil
import os_name
import quiz
from my_banc_account import personal_account


#  посмотреть файлы/папки
def f_list(param):
    only_f = []
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        if param == 'dir_names':
            only_f.extend(dirnames)
            f = 'папки'
        elif param == 'file_names':
            only_f.extend(filenames)
            f = 'файлы'
        break
    print(f'В текущей директории находятся {f}:')
    for i in range(len(only_f)):
        print((only_f[i]))

while True:
    print('*' * 30)
    print(' 1. создать папку ')
    print(' 2. удалить папку')
    print(' 3. копировать файл')
    print(' 4. просмотр содержимого рабочей директории')
    print(' 5. посмотреть только папки')
    print(' 6. посмотреть только файлы')
    print(' 7. просмотр информации об операционной системе')
    print(' 8. создатель программы')
    print(' 9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход ')
    print('*' * 30)

    choice = input('Выберите пункт меню ')
    if choice == '1':
        folder_name = input('Дайте имя папки - ')
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        else:
            print(f'Папка {folder_name} уже есть')
    elif choice == '2':
        folder_name = input('Какую папку хотите удалить? ')
        os.rmdir(folder_name)
    elif choice == '3':
        folder_name = input('Какой файл хотите копировать? ')
        shutil.copy(folder_name, 'file_copy')
    elif choice == '4':
        directory = os.getcwd()
        print(f'В текущей директории {directory} находятся: ')
        for i in range(len(os.listdir(directory))):
            print(os.listdir(directory)[i])
    elif choice == '5':
        f_list('dir_names')
    elif choice == '6':
        f_list('file_names')
    elif choice == '7':
        print(os_name.my_os())
    elif choice == '8':
        print('информация об авторе - id2k1149@gmail.com')
    elif choice == '9':
        print(quiz.quiz())
    elif choice == '10':
        personal_account()
    elif choice == '11':
        break
    else:
        print('Неверный пункт меню')
