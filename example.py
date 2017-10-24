import pandas as pd
import numpy as np

data = pd.read_csv('GTDdataset.csv', encoding='latin1', low_memory=False)

result = (data['crit1'] == 1) & (data['crit2'] == 1) & (data['crit3'] == 1)

print(data[result])

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)
# print(len(result[['eventid', 'country_txt', 'attacktype1_txt', 'weaptype1_txt', 'targtype1_txt']][:]))
