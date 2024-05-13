# поиск и удаление лишних символов из файла


def delete_f(file,change):

    with open(file, 'r', encoding='utf-8') as f:          
        book = f.readlines()
        s=''.join(book)
    with open(file, 'w', encoding='utf-8') as f:
        if change != 1:    
             s = s.replace('\n\n\n','\n\n')              #  удаляем лишние переходы между строками
             f.writelines(s)
        elif change == 1:
             s = s.replace('\n\n\n','\n\n')              #  удаляем лишние переходы между строками
             s = s.replace('\n', '', 1)
             f.writelines(s)