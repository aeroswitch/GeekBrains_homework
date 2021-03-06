'''
6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например  название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''

goods = []
n = 1
while True:
    question = input('Хотите добавить товар? Введите "да" для добавления или "нет" для выхода из меню добавления '
                     'товаров: ').lower()
    if question == 'да':
        product_full_desc = [n]
        product_specifications = {}
        title = input('Название товара: ').lower()
        price = int(input('Стоимость: '))
        quantity = int(input('Количество: '))
        unit = input('Единица измерения: ').lower()
        product_specifications['название'] = title
        product_specifications['цена'] = price
        product_specifications['количество'] = quantity
        product_specifications['ед'] = unit
        product_full_desc.append(product_specifications)
        product_full_desc = tuple(product_full_desc)
        goods.append(product_full_desc)
        print('Товар успешно добавлен в каталог!')
        n += 1
    elif question == 'нет':
        break
    else:
        print('Неправильная команда')

if goods:
    print('-' * 10)
    print('Текущий каталог товаров:')
    # для более красивого построчного вывода сделаем это через цикл
    for i in goods:
        print(i)
else:
    print('Каталог товаров пуст')

# формируем аналитику товаров
titles = []
prices = []
quantities = []
units = []

for i in range(len(goods)):
    titles.append(goods[i][1].get('название'))
    prices.append(goods[i][1].get('цена'))
    quantities.append(goods[i][1].get('количество'))
    units.append(goods[i][1].get('ед'))

# удаляем возможные дубликаты в списке аналитики о товарах
titles = list(set(titles))
prices = list(set(prices))
quantities = list(set(quantities))
units = list(set(units))

# сортируем списки для упорядоченного отображения в финальном словаре аналитики о товарах
titles.sort()
prices.sort()
quantities.sort()
units.sort()

analytics = {
    'названия': titles,
    'цены': prices,
    'количества': quantities,
    'ед': units
}
print('-' * 10)
print('аналитика о товарах:')
# для более красивого построчного вывода сделаем это через цикл
for key, val in analytics.items():
    print(f'{key}: {val}')
print('-' * 10)

#  -------------------------------------------------------- 6 ----------------------------------------------------------


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        _ = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
        features[f] = int(_) if (f == 'цена' or f == 'количество') else _  # Меняем тип числовых свойства
        analytics[f].append(features[f])  # Добавляем свойство в аналитику
    goods.append((num, features))  # Добавляем свойство в список товаров
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*" * 30)

#  ------------------------------------------- вариант решения ---------------------------------------------------------


i = 1
database = []
analytics = []
list_ = dict()

while True:
    start = input("Hi! I'm a database of goods. If you want to continue, enter 1. Finish - 0.\n -- ")
    if start == "0":
        l = []
        print("Do you want to do analytics?")
        answer = input("Yes - y, No - n ")
        while answer == "y":
            type_ = input("Enter analytics parameter: name, price, number, units - ")
            for j in range(len(database)):
                l.append(analytics[j].get(type_))
                list_[type_] = l
            answer = input("Do you want continue? Yes - y, No - n ")
        if answer == "n":
            if database:
                print(database)
            else:
                print("You have left the program")
        else:
            print("You mast enter 'y' or 'n'")
        print(database)
        print(list_)
        break
    elif start == "1":
        good_ = dict()
        good_["name"] = input("Enter name of good - ")
        good_["price"] = input("Enter price of good - ")
        good_["number"] = input("Enter number of good - ")
        good_["units"] = input("Enter units of good - ")
        database.append((i, good_))
        analytics.append(good_)
        i += 1
    else:
        print("You didn't enter the required numbers - 0 or 1.")

#  ------------------------------------------- вариант решения ---------------------------------------------------------

enter = ''
goods = []
i = 0

while enter == '':  # если нажата клавиша Enter - вводим данные, иначе выходим
    i += 1

    name = input('\nEnter name of good: ')
    price = input('Enter price: ')
    num = input('Enter quantity of good: ')
    unit = input('Enter unit: ')

    goods.append((i, {'name': name, 'price': price, 'num': num, 'unit': unit}))
    print('\n', goods)

    enter = input('\nPress Enter for continue, any key+Enter to exit...')

# вывод "аналитики"
while True:
    print('\nChoose action: ')
    print(' [1] Print list of goods.')
    print(' [2] Print list of prices.')
    print(' [3] Print quantities.')
    print(' [4] Print units.')
    print(' [5] Exit.')

    action = input('\nYour choice: ')
    if action == '5':
        break

    names = ('Goods', 'Prices', 'Quantities', 'Units')
    titles = ('name', 'price', 'num', 'unit')
    res = {'name': [], 'price': [], 'num': [], 'unit': set()}

    for id, v in goods:
        res['name'].append(v['name'])
        res['price'].append(v['price'])
        res['num'].append(v['num'])
        res['unit'].add(v['unit'])

    print(res)

    print(f'\n{names[int(action) - 1]}: {res[titles[int(action) - 1]]}')

print('\nGoodbye!')