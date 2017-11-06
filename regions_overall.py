"""
Regions frequency all year graph generator module
"""

# Third-party libraries import
import pandas as pd
import pygal

# Custom modules import
import regions_main


def frequency(data):
    """ Main generate function get data and weapon id = 0 (Overall) """
    # Graph generate goes here!
    # Export file name as Weapons_Frequency_Overall

    regions = {
        1: "North America",
        2: "Central America & Caribbean",
        3: "South America",
        4: "East Asia",
        5: "Southeast Asia",
        6: "South Asia",
        7: "Central Asia",
        8: "Western Europe",
        9: "Eastern Europe",
        10: "Middle East & North Africa",
        11: "Sub-Saharan Africa",
        12: "Australasia & Oceania"
    }

    result_x = [regions[x] for x in sorted(regions)]
    result_y = []

    for x in sorted(regions):
        freq = len(data[data['region'] == x])
        result_y.append(freq)

    chart = pygal.Bar(show_minor_x_labels=False, truncate_legend=40,
                      truncate_label=20, x_label_rotation=90, logarithmic=True, y_labels_major_every=3,
                      show_minor_y_labels=False)

    chart.x_labels = []

    chart.title = 'Overall incidents from 1970 to 2016 except 1993 by regions'

    for x in range(12):
        chart.add(result_x[x] + " (" + str(result_y[x]) + ")", result_y[x])

    chart.render_to_file('Charts/Regions_Frequency_Overall.svg')

    # End of modules and return back to main
    print("\nGraph generated!\n")
    regions_main.main(data)


def success(data):
    """ Main generate function get data and weapon id = 0 (Overall) """
    # Graph generate goes here!
    # Export file name as Weapons_SuccessRate_Overall

    regions = {
        1: "North America",
        2: "Central America & Caribbean",
        3: "South America",
        4: "East Asia",
        5: "Southeast Asia",
        6: "South Asia",
        7: "Central Asia",
        8: "Western Europe",
        9: "Eastern Europe",
        10: "Middle East & North Africa",
        11: "Sub-Saharan Africa",
        12: "Australasia & Oceania"
    }
    result_x = [regions[x] for x in sorted(regions)]
    result_y = []

    for x in sorted(regions):
        if len(data[data['region'] == x]) == 0:
            freq = 0
        else:
            freq = len(data[(data['region'] == x) & (data['success'] == 1)]) / len(data[data['region'] == x])
        result_y.append(freq)

    chart = pygal.Bar(show_minor_x_labels=False, truncate_legend=40,
                      truncate_label=20, x_label_rotation=90, y_labels_major_every=3,
                      show_minor_y_labels=False)

    chart.x_labels = []

    chart.title = 'Overall success rate by regions from 1970 to 2016 except 1993'

    for x in range(12):
        if result_y[x] == 0:
            continue
        chart.add(result_x[x] + " (" + str("%.3f" % (result_y[x] * 100)) + "%)", round(result_y[x] * 100, 3))

    chart.render_to_file('Charts/Regions_SuccessRate_Overall.svg')

    # End of modules and return back to main
    print("\nGraph generated!\n")
    regions_main.main(data)
