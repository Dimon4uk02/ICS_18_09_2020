import matplotlib.pyplot as plt
from numpy import *
import numpy as np
from FinalProject.convert_efficiency_to_json import dict_of_data_for_plot
import json

dict_of_values_for_plots = {}

for key, val in dict_of_data_for_plot.items():
    for val_key, val_value in val.items():
        try:
            dict_of_values_for_plots[val_key].append(val_value)
        except:
            dict_of_values_for_plots[val_key] = [val_value]

styles = ['b--', 'k', 'r--']
line_width = ['1', '5', '2']
for final_key, final_val in dict_of_values_for_plots.items():
    if final_key != 'period':
        for id, val in enumerate(dict_of_values_for_plots[final_key]):
            print(val)
            plt.plot(val, styles[id], linewidth=line_width[id], alpha=0.7)
        plt.legend(['Дніпрянка', 'Універсам 22', 'Універсам 23'])
        plt.savefig(final_key, dpi=200)
        plt.clf()

