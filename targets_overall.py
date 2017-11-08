"""
Weapons frequency all year graph generator module
"""

# Third-party libraries import
import pandas as pd
import pygal
from math import isnan

# Custom modules import
import targets_main


def frequency(data):
    """ Main generate function get data and weapon id = 0 (Overall) """
    # Graph generate goes here!
    # Export file name as Targets_Frequency_Overall

    targets = {
        1: "Business",
        2: "Government (General)",
        3: "Police",
        4: "Military",
        5: "Abortion Related",
        6: "Airports & Aircraft",
        7: "Government (Diplomatic)",
        8: "Educational Institution",
        9: "Food or Water Supply",
        10: "Journalists & Media",
        11: "Maritime",
        12: "NGO",
        13: "Other",
        14: "Private Citizen & Property",
        15: "Religious",
        16: "Telecommunication",
        17: "Terrorists/Non-State Militias",
        18: "Tourists",
        19: "Transportation",
        20: "Unknown",
        21: "Utilities",
        22: "Violent Political Parties"
    }
    result_x = [targets[x] for x in sorted(targets)]
    result_y = []

    for x in sorted(targets):
        freq = len(data[data['targtype1'] == x])
        result_y.append(freq)

    chart = pygal.Bar(show_minor_x_labels=False, truncate_legend=40,
                      truncate_label=20, x_label_rotation=90, logarithmic=True, y_labels_major_every=3,
                      show_minor_y_labels=False)

    chart.x_labels = []

    chart.title = 'Overall incidents by target categories from 1970 to 2016 except 1993'

    for x in range(22):
        chart.add(result_x[x] + " (" + str(result_y[x]) + ")", result_y[x])

    chart.render_to_file('Charts/Targets_Frequency_Overall.svg')

    # End of modules and return back to main
    print("\nGraph generated!")
    targets_main.main(data)


def success(data):
    """ Main generate function get data and weapon id = 0 (Overall) """
    # Graph generate goes here!
    # Export file name as Targets_Frequency_SuccessRate

    targets = {
        1: "Business",
        2: "Government (General)",
        3: "Police",
        4: "Military",
        5: "Abortion Related",
        6: "Airports & Aircraft",
        7: "Government (Diplomatic)",
        8: "Educational Institution",
        9: "Food or Water Supply",
        10: "Journalists & Media",
        11: "Maritime",
        12: "NGO",
        13: "Other",
        14: "Private Citizen & Property",
        15: "Religious",
        16: "Telecommunication",
        17: "Terrorists/Non-State Militias",
        18: "Tourists",
        19: "Transportation",
        20: "Unknown",
        21: "Utilities",
        22: "Violent Political Parties"
    }
    result_x = [targets[x] for x in sorted(targets)]
    result_y = []

    for x in sorted(targets):
        if len(data[data['targtype1'] == x]) == 0:
            freq = 0
        else:
            freq = len(data[(data['targtype1'] == x) & (data['success'] == 1)]) / len(data[data['targtype1'] == x])
        result_y.append(freq)

    chart = pygal.Bar(show_minor_x_labels=False, truncate_legend=40,
                      truncate_label=20, x_label_rotation=90, y_labels_major_every=3,
                      show_minor_y_labels=False)

    chart.x_labels = []

    chart.title = 'Overall success rate by targets from 1970 to 2016 except 1993'

    for x in range(22):
        if result_y[x] == 0:
            continue
        chart.add(result_x[x] + " (" + str("%.3f" % (result_y[x] * 100)) + "%)", round(result_y[x] * 100, 3))

    chart.render_to_file('Charts/Targets_Frequency_SuccessRate.svg')

    # End of modules and return back to main
    print("\nGraph generated!")
    targets_main.main(data)


def victims(data):
    """ Horizontal Bar chart show highest Victim in categories """

    targets = {
        1: "Business",
        2: "Government (General)",
        3: "Police",
        4: "Military",
        5: "Abortion Related",
        6: "Airports & Aircraft",
        7: "Government (Diplomatic)",
        8: "Educational Institution",
        9: "Food or Water Supply",
        10: "Journalists & Media",
        11: "Maritime",
        12: "NGO",
        13: "Other",
        14: "Private Citizen & Property",
        15: "Religious",
        16: "Telecommunication",
        17: "Terrorists/Non-State Militias",
        18: "Tourists",
        19: "Transportation",
        20: "Unknown",
        21: "Utilities",
        22: "Violent Political Parties"
    }

    result_x = [targets[x] for x in sorted(targets)]
    result_y = []

    for x in sorted(targets):
        maximum = max(data[data['targtype1'] == x]['nkill'])
        if isnan(maximum):
            result_y.append(0)
            continue
        freq = data[(data['targtype1'] == x) & (data['nkill'] == maximum)].nkill.values[0]
        result_y.append(freq)

    # Initialize Line Chart
    chart = pygal.HorizontalBar(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40,
                                truncate_label=20)
    # Chart title
    chart.title = 'Compare the most victims incident by targets'
    # X-Axis Label
    chart.x_labels = []
    # Y-Axis and label
    for i in range(22):
        if result_y == 0:
            continue
        chart.add(result_x[i], result_y[i])

    # Save chart into file
    filename = 'Charts/Targets_Compare_Maximum_Victims.svg'
    chart.render_to_file(filename)

    # End of modules and return back to main
    print("\nGraph generated!")
    targets_main.main(data)
