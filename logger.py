from create_data import name_data, surname_data, phone_data, address_data
from delete_from_file import delete_f

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'В каком варианте записывать данные:\n\n'
    f'1 Вариант: \n'
    f'{name}\n {surname}\n {phone} \n {address}\n\n'
    f'2 Вариант: \n'
    f'{name};{surname};{phone};{address}\n'
    f'Выберете вариант: '))

    while var != 1 and var != 2:
        print("Вы ввели некорректные данные. \n Введите 1 для работы в режиме записи. \n Введите 2 для работы в режиме чтения")
        var = int(input())
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))

    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_sec = f.readlines()
        print(*data_sec)

def change_data():

    var = int(input('Введите "1", если хотите работать с первым файлом и "2" для работы со вторым файлом '))
    while var != 1 and var != 2:
        print("Вы ввели некорректные данные. \n Введите 1 с первым файлом \n Введите 2 для работы со вторым файлом ")
        var = int(input())

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first=f.readlines()
            change = int(input("Введите номер записи, которую требуесят изменить: "))

            data_first_list = []
            j = 0

            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:       
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j=i

            while change > len(data_first_list):
                print("Записи с таким индексом не существует. Введите корретный номер записи:")
                change = int(input())
  
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        
        data_first_list.pop(change-1)
        data_first_list.insert(change-1, ''.join(f'{name}\n{surname}\n{phone}\n{address}\n'))
        
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_first_list)):
                f.write(data_first_list[i])

        delete_f('data_first_variant.csv',0)
        
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_sec = f.readlines()

        data_sec_list = []
        
        j = 0
        for i in range(len(data_sec)):
            if data_sec[i] == '\n' or i == len(data_sec) - 1:
                data_sec_list.append(''.join(data_sec[j:i+1]))
                j=i

        change = int(input("Введите номер записи, которую требуесят изменить: "))
            
        while change > len(data_sec_list):
                print("Записи с таким индексом не существует. Введите корретный номер записи:")
                change = int(input())

        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()        

        data_sec_list.pop(change-1)
        data_sec_list.insert(change-1, ''.join(f'{name};{surname};{phone};{address}\n'))
        
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_sec_list)):
                f.write(data_sec_list[i])

        delete_f('data_second_variant.csv',0)


def delete_data():
    var = int(input('Введите "1", если хотите работать с первым файлом и "2" для работы со вторым файлом '))
    while var != 1 and var != 2:
        print("Вы ввели некорректные данные. \n Введите 1 с первым файлом \n Введите 2 для работы со вторым файлом ")
        var = int(input())

    if var == 1:

        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first=f.readlines()
            change = int(input("Введите номер записи, которую требуесят удалить: "))

            data_first_list = []
            j = 0

        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:       
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i

        while change > len(data_first_list):
            print("Записи с таким индексом не существует. Введите корретный номер записи:")
            change = int(input())
            
        data_first_list.pop(change-1)
        
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_first_list)):
                f.write(data_first_list[i])

        delete_f('data_first_variant.csv',change)
    
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_sec = f.readlines()

        data_sec_list = []
        
        j = 0
        for i in range(len(data_sec)):
            if data_sec[i] == '\n' or i == len(data_sec) - 1:
                data_sec_list.append(''.join(data_sec[j:i+1]))
                j=i

        change = int(input("Введите номер записи, которую требуесят удалить:"))
            
        while change > len(data_sec_list):
                print("Записи с таким индексом не существует. Введите корретный номер записи:")
                change = int(input()) 

        data_sec_list.pop(change-1)
        
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_sec_list)):
                f.write(data_sec_list[i])

        delete_f('data_second_variant.csv',change)
