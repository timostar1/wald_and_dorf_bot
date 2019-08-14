from ingredients_calculator import ingredients_calculator
from dish_parser import dish_parser
'''
print(ingredients_calculator({'салат с зеленью': 1, 'салат с кукурузой и зеленью': 1}))
print(ingredients_calculator({'каша кукурузная': 1}))
print(ingredients_calculator({'омлет': 1}))
'''
a, b = dish_parser('Салат с зеленью 1 \n рисовая каша 4 \n Борщ с тушёнкой 3')
print(ingredients_calculator(a))
print(ingredients_calculator({'каша кукурузная': 1}))