"""
Weapons frequency all year graph generator module
"""


# Third-party libraries import
import pandas as pd
import pygal

# Custom modules import
import weapons_main

def main(data, weapon):
    """ Main generate function get data and weapon id """
    # Graph generate goes here!
    # Export file name as Weapons_Frequency_<weapon_id>

    weapons = {
        1: "Biological",
        2: "Chemical",
        3: "Radiological",
        4: "Nuclear",
        5: "Firearms",
        6: "Explosives",
        7: "Fake Weapons",
        8: "Incendiary",
        9: "Melee",
        10: "Sabotage Equipment",
        11: "Other",
        12: "Overall",
        13: "Unknown"
    }
    
    result_x = [x for x in range(1970, 2017) if x != 1993]
    result_y = []

    for year in result_x:
        frequency = len(data[(data['iyear'] == year) & (data['weaptype1'] == weapon)])
        result_y.append(frequency)

    # Initialize Line Chart
    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=20)

    # Chart title
    chart.title = 'Terriorism incidents of ' + weapons[weapon] + ' from 1970 to 2016 except 1993'

    # X-Axis Label
    chart.x_labels = [str(x) for x in result_x]

    # Y-Axis and label
    chart.add('Incidents count', result_y)
    
    # Save chart into file
    filename = 'Charts/Weapons_Frequency_' + weapons[weapon] + '.svg'
    chart.render_to_file(filename)

    # End of modules and return back to main
    print("\nGraph generated!\n")
    weapons_main.main(data)
