"""
Regions frequency all year graph generator module
"""


# Third-party libraries import
import pandas as pd
import pygal as pg


# Custom modules import
import regions_main


def main(data, region):
    """ Main generate function get data and region id """
    # Graph generate goes here!
    # Export file name as Regions_Frequency_<region_id>
    result_x = [x for x in range(1970, 2017) if x != 1993]
    result_y = []

    for year in result_x:
        frequency = len(data[(data['iyear'] == year) & (data['region'] == region)])
        result_y.append(frequency)

    # Initialize Line Chart
    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=20)
    # Chart title
    chart.title = 'Terriorism success rate of overall regions from 1970 to 2016 except 1993 (in %)'
    # X-Axis Label
    chart.x_labels = [str(x) for x in result_x]
    # Y-Axis and label
    chart.add('Success rate (%)', result_y)
    # Range of Y-Axis value
    chart.range = [0, 100]
    # Save chart into file
    chart.render_to_file('chart.svg')

    # Pandas display setting to show all row of data
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', None)
    # End of modules and return back to main
    print("\nGraph generated!\n")
    regions_main.main(data)
