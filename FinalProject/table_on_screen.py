# @copyright САКУН_ВЛАДИСЛАВ_ОЛЕКСАНДРОВИЧ_ФІТ_1КУРС_4ГРУПА


from prettytable import PrettyTable
from FinalProject.data import data_array

x = PrettyTable()

x.field_names = ['Код', 'Період', 'Товарообіг', 'Балансовий прибуток', 'Середньорічна вартість основних засобів']

for enterprise_activity in data_array:
    x.add_row([enterprise_activity.code, enterprise_activity.period,
               enterprise_activity.commodity_circulation,
               enterprise_activity.balance_income,
               enterprise_activity.average_cost_main_components])

print(x)
