from pprint import pprint

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 6, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Помидор', 'quantity': 4, 'measure': 'шт'},
    ]
}


def get_shop_list_by_dishes(dishes, number_of_person=1):
    resulted = {}

    for Ingredients_list in dishes.values():
        for Ingredients_dict in Ingredients_list:
            keys = []
            values = []
            keys += Ingredients_dict.keys()
            values += Ingredients_dict.values()
            ingredient_count = values[1] * number_of_person
            if values[0] in resulted.keys():
                resulted[values[0]][keys[1]] += ingredient_count
                continue
            resulted[values[0]] = {keys[1]: ingredient_count, keys[2]: values[2]}

    return resulted


pprint(get_shop_list_by_dishes(cook_book, 2))