from dataclasses import dataclass
import json
import os
import codecs


@dataclass
class Enterprise:
    code: int
    name: str


@dataclass
class EnterpriseActivity:
    code: int
    period: str
    commodity_circulation: float
    balance_income: float
    average_cost_main_components: float


def printEnterpriseActivity(enterpriseActivity):
    '''printEnterpriseActivity function prints
    "Основні показники діяльності підприємств"
    with names and values'''

    print("Код {code}, Період {period}, Товарообіг,грн. {commodity_circulation}, Балансовий прибуток,грн. {balance_income} Середньорічна вартість основних засобів, грн. {average_cost_main_components}"
          .format(code=enterpriseActivity.code, period=enterpriseActivity.period, commodity_circulation=enterpriseActivity.commodity_circulation,
                  balance_income=enterpriseActivity.balance_income, average_cost_main_components=enterpriseActivity.average_cost_main_components))


# Json was made by TABULA https://tabula.technology
with codecs.open("Lab4\\data\\tabula-zad19.json", "r", 'utf-8') as f:
    distros_dict = json.load(f)

data_array = []

# parse json to array of EnterpriseActivity
for distro in distros_dict:
    data_list = distro['data']

    for data in data_list:
        data_array.append(EnterpriseActivity(int(data[0]["text"]), str(data[1]["text"]), float(str(data[2]["text"]).replace(',', '.')),
                                             float(str(data[3]["text"]).replace(',', '.')), float(str(data[4]["text"]).replace(',', '.'))))


enterprises_array = []
enterprises_array.append(Enterprise(1, "Універсам 22"))
enterprises_array.append(Enterprise(2, "Дніпрянка"))
enterprises_array.append(Enterprise(3, "Універсам 23"))

print('Docstring: \n {}'.format(printEnterpriseActivity.__doc__) )
print('-' * 20)

print('Size {} \n'.format((len(data_array))))
for data in data_array:
    printEnterpriseActivity(data)
