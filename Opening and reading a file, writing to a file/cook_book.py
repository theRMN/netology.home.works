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


def show_dish_list(dishes=None):
    if dishes is None:
        dishes = cook_book

    dish_list = []
    new_dishes = {}

    print('Доступные блюда:\n================')

    for dish_name in enumerate(dishes, 1):
        dish_list += ([dish_name[0]] + [dish_name[1]])
        print(str(dish_name[0]) + '.', dish_name[1])

    user_choice_list = input('================\nВыберите блюдо: ').split(', ')

    for user_choice in user_choice_list:
        if user_choice in dish_list:
            for dish in dishes.items():
                if user_choice == dish[0]:
                    new_dishes[dish[0]] = dish[1]
        else:
            return dishes

    return new_dishes


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

    print('================\nИнгридиенты для выбранных блюд:\n================')

    return pprint(resulted)


def program():
    x = show_dish_list()

    user_input = int(input('================\nВведите количество персон: '))

    get_shop_list_by_dishes(x, user_input)


program()
