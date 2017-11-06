import pandas as pd
import numpy as np
import pygal as pg

# Import dataset from CSV into pandas dataframe
data = pd.read_csv('GTDdataset.csv', encoding='latin1', low_memory=False)

# Data select condition
result_x = [x for x in range(1970, 2017) if x != 1993]
result_y = []

for year in result_x:
    success = (len(data[(data['success'] == 1) & (data['iyear'] == year)]) / len(data[data['iyear'] == year])) * 100
    result_y.append(success)

# Initialize Line Chart
chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=20)
# Chart title
chart.title = 'Overall success rate from 1970 to 2016 except 1993 (in %)'
# X-Axis Label
chart.x_labels = [str(x) for x in result_x]
# Y-Axis and label
chart.add('Success rate (%)', result_y)
# Range of Y-Axis value
chart.range = [60, 100]
# Save chart into file
chart.render_to_file('chart.svg')

# Pandas display setting to show all row of data
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', None)
