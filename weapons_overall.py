"""
Weapons frequency all year graph generator module
"""

# Third-party libraries import
import pygal

# Custom modules import
import weapons_main


def frequency(data, test=False):
    """ Main generate function get data and weapon id = 0 (Overall) """
    # Graph generate goes here!
    # Export file name as Weapons_Frequency_Overall

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
    result_x = [weapons[x] for x in sorted(weapons)]
    result_y = []

    for x in sorted(weapons):
        freq = len(data[data['weaptype1'] == x])
        result_y.append(freq)

    chart = pygal.Bar(show_minor_x_labels=False, truncate_legend=40,
                      truncate_label=20, x_label_rotation=90, logarithmic=True, y_labels_major_every=3,
                      show_minor_y_labels=False)

    chart.x_labels = []

    chart.title = 'Overall usage by weapon categories from 1970 to 2016 except 1993'

    for x in range(13):
        chart.add(result_x[x] + " (" + str(result_y[x]) + ")", result_y[x])

    chart.render_to_file('Charts/Weapons_Frequency_Overall.svg')

    # End of modules and return back to main
    if test:
        return
    print("\nGraph generated!\n")
    weapons_main.main(data)


def success(data, test=False):
    """ Main generate function get data and weapon id = 0 (Overall) """
    # Graph generate goes here!
    # Export file name as Weapons_Frequency_SuccessRate

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
    result_x = [weapons[x] for x in sorted(weapons)]
    result_y = []

    for x in sorted(weapons):
        if len(data[data['weaptype1'] == x]) == 0:
            freq = 0
        else:
            freq = len(data[(data['weaptype1'] == x) & (data['success'] == 1)]) / len(data[data['weaptype1'] == x])
        result_y.append(freq)

    chart = pygal.Bar(show_minor_x_labels=False, truncate_legend=40,
                      truncate_label=20, x_label_rotation=90, y_labels_major_every=3,
                      show_minor_y_labels=False)

    chart.x_labels = []

    chart.title = 'Overall success rate by weapon categories from 1970 to 2016 except 1993'

    for x in range(13):
        if result_y[x] == 0:
            continue
        chart.add(result_x[x] + " (" + str("%.3f" % (result_y[x] * 100)) + "%)", round(result_y[x] * 100, 3))

    chart.render_to_file('Charts/Weapons_SuccessRate_Overall.svg')

    # End of modules and return back to main
    if test:
        return
    print("\nGraph generated!\n")
    weapons_main.main(data)
