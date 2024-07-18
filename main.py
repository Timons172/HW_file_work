import pprint
import os


# Задача №1
def file_read():
    """
    Формируется словарь из файла
    :return: Словарь (блюдо: необходимые ингредиенты)
    """
    cook_book = {}
    with open("files/recipes.txt") as file:
        for line in file:
            product_list = []
            dish = line.strip()
            product_count = int(file.readline().strip())
            for idx in range(product_count):
                ingredient = file.readline().strip()
                ingredient_name, quantity, measure = ingredient.strip().split(' | ')
                product = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                product_list.append(product)
                cook_book[dish] = product_list
            file.readline().strip()
    return cook_book


# Задача №2
def get_shop_list_by_dishes(dishes, person_count):
    """
    Формируется словарь с необходимыми продуктами для приготовления блюд
    :param dishes: Список блюд
    :param person_count: Количество персон
    :return: Словарь (Продукт: необходимое количество)
    """
    cook_book = file_read()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            product_list = cook_book[dish]
            for product in product_list:
                if product['ingredient_name'] in shop_list:
                    shop_list[product['ingredient_name']]['quantity'] += int(product['quantity']) * person_count
                else:
                    shop_list[product['ingredient_name']] = {'measure': product['measure'],
                                                             'quantity': (int(product['quantity']) * person_count)}
        else:
            print(f"Блюда '{dish}' в книге рецептов нет!")
    return shop_list


# Задача №3
def story_read():
    """
    Формируется отсортированный словарь из файлов по ключу: количество строк в исходном файле
    :return: Словарь (Количество строк: название файла с количеством строк и данными из файла)
    """
    story_dict = {}
    path = 'files/story/'
    txt_list = os.listdir(path)
    for txt in txt_list:
        with open(path + txt) as file:
            data = file.readlines()
            line_count = len(data)
            readable_data = ''.join(data)
        story_dict[line_count] = f'{txt}\n{line_count}\n{readable_data}'
    sorted_dict = dict(sorted(story_dict.items(), key=lambda x: x[0]))
    return sorted_dict


def story_write(dict_):
    """
    Формируется файл из переданного словаря
    :param dict_: Отсортированный словарь по ключу: количество строк в исходном файле
    :return: Файл с записанными данными: Название исходного файла, количество строк, данные из исходного файла
    """
    path = 'files/sorted story/'
    with open(path + 'sorted_story.txt', 'w', encoding='utf-8') as file:
        for value in dict_.values():
            file.write(value + '\n')
        print("Файл записан")


# Вызов функций для решения задач №1 и №2
pprint.pprint(file_read())
print()
pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()

# Вызов функций для решения задачи №3
story_write(story_read())
