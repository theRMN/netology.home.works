from pprint import pprint


def making_cook_book():
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        line_list = []
        count = 0

        for line in f:
            try:
                line = int(line)
                line_list.append(line)
                count = len(line_list)
            except:
                continue

    with open('recipes.txt', 'r', encoding='utf-8') as f:
        cook_book = {}
        ingredient_list = []

        while count > 0:
            dish_name = f.readline().strip()
            ingredient_count = int(f.readline().strip())

            for _ in range(ingredient_count):
                m = f.readline().strip().split('|')

                ingredient_list += [{'ingredient_name': m[0], 'quantity': m[1], 'measure': m[2]}]

            cook_book[dish_name] = ingredient_list
            ingredient_list = []
            f.readline().strip()
            count -= 1

    return cook_book


def show_dish_list(dishes=None):
    if dishes is None:
        dishes = making_cook_book()

    dish_list = []
    new_dishes = {}

    print('Доступные блюда:\n================')

    for dish_name in enumerate(dishes, 1):
        dish_list += ([dish_name[0]] + [dish_name[1]])
        print(str(dish_name[0]) + '.', dish_name[1])

    print('================\nДля выбора всех доступных блюд, нажмите "Enter"')

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
            ingredient_count = int(values[1]) * number_of_person

            if values[0] in resulted.keys():
                resulted[values[0]][keys[1]] += ingredient_count
                continue

            resulted[values[0]] = {keys[1]: ingredient_count, keys[2]: values[2]}

    print('================\nИнгридиенты для выбранных блюд:\n================')

    return pprint(resulted)


def program():
    x = show_dish_list()

    user_input = input('================\nВведите количество персон: ')
    try:
        user_input = int(user_input)
    except ValueError:
        print('================\nОшибка! Количество персон не может быть:', user_input)
        quit()

    get_shop_list_by_dishes(x, user_input)


program()
