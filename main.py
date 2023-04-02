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

pprint(cook_book, sort_dicts=False)


