import pandas as pd
import numpy as np
import pygal
def target_part():
    data = pd.read_csv('GTDdataset.csv', encoding='latin1', low_memory=False)
    data_part = data['targtype1_txt']
    all_target = [target_n for target_n in data_part]
    target = []
    info = []
    for target_n in data_part:
        if target_n not in target:
            target.append(target_n)
            info.append(all_target.count(target_n)/len(all_target) * 100)
    chart = pygal.Pie()
    chart.title = 'All Main Targets of Terrorists from 1970 to 2016 (Except 1993) (in per cent)'
    for i in range(len(target)):
        chart.add(target[i], info[i])
    chart.render_to_file('chart_of_target.svg')
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', None)
target_part()
