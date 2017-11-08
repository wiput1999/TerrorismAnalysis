"""
Weapons success rate all year graph generator module
"""


# Third-party libraries import
import pandas as pd
import pygal as pg


# Custom modules import
import weapons_main


def main(data, weapon):
    """ Main generate function get data and weapon id """
    # Graph generate goes here!
    # Export file name as Weapon_Success_<weapon_id>
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
        success = (len(data[(data['success'] == 1) & (data['weaptype1'] == weapon) & (data['iyear'] == year)]) / len(data[data['iyear'] == year])) * 100
        result_y.append(success)

    # Initialize Line Chart
    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True,
                    truncate_label=20 , value_formatter=lambda x: "%d%%" %(x))
    # Chart title
    chart.title = str(weapons[weapon]) + ' weapon success rate from 1970 to 2016 except 1993 (in %)'
    # X-Axis Label
    chart.x_labels = [str(x) for x in result_x]
    # Y-Axis and label
    chart.add('Success rate (%)', result_y)
    # Range of Y-Axis value
    chart.range = [0, max(result_y)+5]
    # Save chart into file
    filename = 'Charts/Weapons_SuccessRate_' + weapons[weapon] + '.svg'
    chart.render_to_file(filename)
    # End of modules and return back to main
    print("\nGraph generated!\n")

    weapons_main.main(data)
