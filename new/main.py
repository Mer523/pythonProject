from pprint import pprint

with open('data.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        cook = line.strip()
        recipe = int(file.readline())
        eat = []
        for _ in range (recipe):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            eat.append({
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            })
        file.readline()
        cook_book[cook] = eat


def get_shop_list_by_dishes(dishes, person_count):
    ingridient_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredients in cook_book[dish_name]:
                meas_list = {}
                if ingredients['ingredient_name'] not in ingridient_list:
                    meas_list['measure'] = ingredients['measure']
                    meas_list['quantity'] = int(ingredients['quantity']) * person_count
                    ingridient_list[ingredients['ingredient_name']] = meas_list
                else:
                    ingridient_list[ingredients['ingredient_name']]['quantity'] = ingridient_list[ingredients['ingredient_name']]['quantity'] + \
                                                                     ingredients['quantity'] * person_count

    return ingridient_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))