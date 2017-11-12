"""
Targets success rate all year graph generator module
"""

# Third-party libraries import
import pygal

# Custom modules import
import targets_main


def main(data, target, test=False):
    """ Main generate function get data and target id """

    # Initialize year list
    years = [x for x in range(1970, 2017) if x != 1993]

    # Initialize percent list
    per_cent = []

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
        # Count which success
        success_in_target = len(data[(data['targtype1'] == target) & (data['success'] == 1) & (data['iyear'] == year)])

        # Count all
        success_all = len(data[(data['success'] == 1) & (data['iyear'] == year)])

        # Prevent divided by zero
        if success_all == 0:
            if test:
                return
            print("\nGraph can't generated!")
            targets_main.main(data)

        # Calculate success rate
        success = round((success_in_target / success_all) * 100, 2)

        # Add success rate into list
        per_cent.append(success)

    # Graph generate goes here!
    chart = pygal.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True,
                       truncate_label=20, value_formatter=lambda x: "%.2f%%" % x)

    # Add title into chart
    chart.title = 'Success Rate of %s from 1970 to 2016 (Except 1993) (in percent)' % (targets[target])

    # Add label into chart
    chart.x_labels = [str(x) for x in years]

    # Add data into chart
    chart.add('Success Rate (%)', per_cent)

    # Export file name as Target_Success_<target_id>
    chart.render_to_file('Charts/Targets_Success_%s.svg' % targets[target])

    # End of modules and return back to main
    if test:
        return
    print("\nGraph generated!\n")
    targets_main.main(data)
