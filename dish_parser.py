def dish_parser(message_from_chief):
    '''
    :param message_from_chief:
    :return: to_cook, repeated_dishes
    '''

    # Cписок еды, отправлен боту завпитами.
    # Количество блюд указывается через пробел после названия.
    # Если блюдо одно, то количество не указывается.
    # Каждое новое блюдо начинается с новой строки.
    # Например,
    #       "Борщ 4
    #       Макароны 3
    #       Сырный суп 2".
    # Мы разделим сообщение на список из строк.
    message_from_chief_divided = message_from_chief.split('\n')

    # to_cook - словарь из пар "название блюда - количество блюда"
    to_cook = dict()

    # repeated_dishes - список повторяющихся блюд
    repeated_dishes = set()

    # Функция добавления блюда в to_cook
    def add_dish(name, count):
        if name == '':
            # Если название блюда оказывается пустым, то ничего не делаем
            pass
        elif name in to_cook:
            # Если такое блюдо уже было,
            # То мы сообщим об этом завпитам
            # Добавим его в список repeated_dishes
            repeated_dishes.add(name)

            # И прибавим новое количество к уже имеющемуся в to_cook
            to_cook[name] += count
        else:
            # Если всё хорошо,
            # Добавляем то, что получилось в to_cook
            to_cook[name] = count

    # Для каждого блюда в списке message_from_chief_divided
    for dish in message_from_chief_divided:

        # Очищаем строку от пробелов в начале и в конце
        dish = dish.strip()

        # string_divided - строка, разбитая на слова
        string_divided = dish.split()

        if string_divided == []:
            # Если строка была пустой, то он пропускает её
            pass

        elif string_divided[-1].isdigit():
            # Если последнее слово в ней является числом
            # Мы удаляем его и записываем в отдельную переменную
            dish_count = int(string_divided.pop())
            # А всё остальное, т. е. название блюда - в другую переменную
            dish_name = ' '.join(string_divided)
            add_dish(dish_name, dish_count)


        else:
            # Если же нет,
            # то добавляем всю строку, которая является названием блюда, и количество - 1
            add_dish(dish, 1)

    # Возвращаем to_cook и repeated_dishes
    return to_cook, repeated_dishes
    # Спасибо за внимание
