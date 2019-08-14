from dish_parser import dish_parser
from ingredients_calculator import ingredients_calculator

def find_unit(ingredient):
    if ingredient == 'яйца':
        return 'шт'
    if ingredient == 'молоко':
        return 'л'
    else:
        return 'г'

def to_buy_handler(to_buy):
    answer = 'Чтобы приготовить эти блюда вам понадобится купить:'
    for ingredient in to_buy:
        answer += '\n' + ingredient + ' ' + str(to_buy[ingredient]) + find_unit(ingredient)
    return answer

def unknown_dishes_handler(unknown_dishes):
    if unknown_dishes:
        return 'Следующие блюда не были найдены в таблице блюд, поэтому мы не посчитали их: ' + ', '.join(unknown_dishes)
    else:
        return ''

def repeated_dishes_handler(repeated_dishes):
    if repeated_dishes:
        return 'Следующие блюда повторялись в вашем сообщении, поэтому мы посчитали их больше одного раза: ' + ', '.join(repeated_dishes)
    else:
        return ''

def message_composer(message_from_chief):
    to_cook, repeated_dishes = dish_parser(message_from_chief)
    if to_cook:
        to_buy, unknown_dishes = ingredients_calculator(to_cook)
        if to_buy:
            return to_buy_handler(to_buy) + '\n\n' + unknown_dishes_handler(unknown_dishes) + '\n' + repeated_dishes_handler(repeated_dishes)
        else:
            return 'К сожалению, мы не смогли найти блюда, которые вы написали, в таблице блюд'
    else:
        return 'К сожалению, мы не смогли найти блюд в вашем сообщении'