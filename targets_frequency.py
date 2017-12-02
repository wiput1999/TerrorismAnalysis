"""
Targets frequency all year graph generator module
"""

# Third-party libraries import
import pygal

# Custom modules import
import targets_main


def main(data, target, test=False):
    """ Main generate function get data and target id """

    # Initialize year list
    years = [x for x in range(1970, 2017) if x != 1993]

    # Initialize frequency list
    freq = []

    # Initialize targets list
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
        17: "Terrorists or Non-State Militias",
        18: "Tourists",
        19: "Transportation",
        20: "Unknown",
        21: "Utilities",
        22: "Violent Political Parties"
    }

    # Calculate result
    for year in years:
        frequency = len(data[(data['targtype1'] == target) & (data['iyear'] == year)])
        freq.append(frequency)

    # Graph generate goes here!
    chart = pygal.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True,
                       truncate_label=20)

    # Set chart title
    chart.title = 'Frequency of %s from 1970 to 2016 (Except 1993)' % (targets[target])

    # Set label
    chart.x_labels = [str(x) for x in years]

    # Add data
    chart.add('Frequency (Times)', freq)

    # Export file name as Targets_Frequency_<target_id>
    chart.render_to_file('Charts/Targets_Frequency_%s.svg' % targets[target])

    # End of modules and return back to main
    if test:
        return
    print("\nGraph generated!\n")
    targets_main.main(data)
