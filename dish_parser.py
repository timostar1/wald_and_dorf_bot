def dish_parser(message_from_chief):

    '''
    :param message_from_chief:
    :return: to_cook
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
    
    # Для каждого блюда в списке message_from_chief_divided
    for dish in message_from_chief_divided:

        # Очищаем строку от пробелов в начале и в конце
        dish = dish.strip()

        # string_divided - строка, разбитая на слова
        string_divided = dish.split()

        if string_divided == []:
            # Если строка была пустой, то он пропускает её
            pass

        elif (string_divided[-1].isdigit()):
            # Если последнее слово в ней является числом
            # Мы удаляем его и записываем в отдельную переменную
            dish_count = int(string_divided.pop())
            # А всё остальное, т. е. название блюда - в другую переменную
            dish_name = ' '.join(string_divided)
            # Добавляем то, что получилось в to_cook
            to_cook[dish_name] = dish_count
        else:
            # Если же нет,
            # то добавляем всю строку, которая является названием блюда, и количество - 1
            to_cook[dish] = 1
            
    # Возвращаем to_cook
    return to_cook
    # Спасибо за внимание