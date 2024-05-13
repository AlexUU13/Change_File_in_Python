from logger import input_data, print_data, change_data, delete_data


def interface():
    print("Добрый день! \n Эта программа - бот справочник. Введите режим работы: \n 1 - запись данных \n 2 - чтение данных \n 3 - изменить запись \n 4 - удалить запись")
    command = int(input())
    while command != 1 and command != 2:
        print("Вы ввели некорректные данные. \n Введите 1 для работы в режиме записи. \n Введите 2 для работы в режиме чтения")
        command = int(input())
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
        print(f'Хотите внести изменения в программу? \n 1 - изменить запись \n 2 - удалить запись \n 3 - оставить базу данных без изменений')
        command = int(input())
        while command != 1 and command != 2 and command != 3:
            print("Вы ввели некорректные данные. \n Введите 1 изменения записи. \n Введите 2 для удаления записи \n Введите 3 для завершения работы")
            command = int(input())        
               
        if command == 1:
            change_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            print("Спасибо, что использовали нашу программу!")

    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()