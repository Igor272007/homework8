# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека).
# Использование функций. Ваша программа не должна быть линейной

def work_with_data_list1():
    with open('data_list1.txt', 'a') as data_list1:
        choice = input('to select an action with the data, enter "import", "export", "find":   ')
        if choice == 'import':
            import_data_list1()
        if choice == 'export':
            export_data_list1()
        if choice == 'find':
            find_data_list1()

def import_data_list1():
    with open('data_list1.txt', 'a') as data_list1:
        (name, surname, patronymic, phone_number) = [input(
            'enter name: ' if i == 0 else 'enter surname: '
            if i == 1 else 'enter patronymic   : ' if i == 2 else
            'enter phone number: ')
            for i in range(4)]
        result = (name, surname, patronymic, phone_number)
        list(map(lambda x: data_list1.write(x + '\n\n' if x == phone_number else x + '\n'), result))
        print(result)
        return result

def export_data_list1():
    with open('data_list1.txt', 'r') as data_list1:
        lst = [i[:-1] for i in data_list1.readlines() if i != '\n']
        result = [{i // 4: lst[i:i + 4]} for i in range(0, len(lst), 4)]
        print(result)
        return result


def find_data_list1(name='', surname='', patronymic='', phone_number=''):
    data_list1 = export_data_list1()
    print('Enter any of the specified parameters, you can enter several, or leave them empty:   ')
    (find_name, find_surname, find_patronymic, find_telephone) = [input(
        'Search by name: ' if i == 0 else 'Search by surname: ' if i == 1 else
        'Search by patronymic: ' if i == 2 else 'Search by phone_number: ')

      for i in range(4)]
    global input_data
    input_data = (find_name, find_surname, find_patronymic, find_telephone)
    input_data = dict((i, x) for i, x in enumerate(input_data) if x != '')
    print(input_data)
    result = [d for d in data_list1 if
              all(list(d.values())[0][key] == value for key, value in input_data.items())]
    print(f'found {len(result)} : ', end='')
    [print(list(i.values())[0], end=' ') for i in result]
    print()
    return result

work_with_data_list1()

