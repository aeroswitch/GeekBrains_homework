'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
Выполнить без использования .reverse() и sorted()
'''
my_list = [7, 5, 3, 3, 2]
print(f'Изначальный список:\n{my_list}')
new_element = int(input('Введите новый элемент для добавления в список рейтинга: '))
for i in range(len(my_list)):
    if my_list[-1] >= new_element:
        my_list.append(new_element)
        break
    elif my_list[i] < new_element:
        index = i
        my_list.insert(index, new_element)
        break

print(f'Обновленный список:\n{my_list}')
