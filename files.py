
cook_book_test = dict()
with open('C:/Users/79035/Desktop/py-33/hw-files/recipes.txt', 'r', encoding = 'utf-8') as f:
    n = f.read()
    text = n.split('\n\n')
    for recipes in text:
        recipes_list = recipes.split('\n')
        name_food = recipes_list[0:1:]
        ingr = recipes_list[2::]
        cook_book_test[name_food[0]] = ingr
cook_book = {}
def cook_book_dict(cook_book_list):
    for key, value in cook_book_list.items():
        new_list = []
        for ingredients in value:
            ingredients_list = ingredients.split(' | ')
            new_dict = {}
            new_dict['ingredient_name'] = ingredients_list[0]
            new_dict['quantity'] = ingredients_list[1]
            new_dict['measure'] = ingredients_list[2]
            new_list.append(new_dict)
        cook_book[key] = new_list
    return(cook_book)

print(cook_book_dict(cook_book_test))

cook_book_final = cook_book_dict(cook_book_test)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for key, value in cook_book_final.items():
        if key in dishes:
            for ingridient in cook_book_final[key]:
                shop_list_by_dishes[ingridient['ingredient_name']] = {'measure':ingridient['measure'],'quantity': int(ingridient['quantity']) * person_count }
    return shop_list_by_dishes

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

