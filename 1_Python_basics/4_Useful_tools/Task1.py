"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

import sys

script_name, production_hours, hour_rate, bonus = sys.argv


def salary():
    try:
        return int(production_hours) * int(hour_rate) + int(bonus)
    except ValueError:
        print('Error! Script parameters should be numbers')


print('Hours worked:', production_hours)
print('Rate per hour: ', hour_rate)
print('Bonus: ', bonus)
print(f'Final salary: {salary()}')
