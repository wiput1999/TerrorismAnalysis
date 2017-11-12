"""
Targets success rate all year graph generator module
"""


# Third-party libraries import
import pandas as pd
import pygal


# Custom modules import
import targets_main


def main(data, target):
    """ Main generate function get data and target id """
    years = [x for x in range(1970, 2017) if x != 1993]
    per_cent = []
    targets = {1: "Business", 2: "Government (General)", 3: "Police", 4: "Military", 5: "Abortion Related",
    6: "Airports & Aircraft", 7: "Government (Diplomatic)", 8: "Educational Institution", 9: "Food or Water Supply",
    10: "Journalists & Media", 11: "Maritime", 12: "NGO", 13: "Other", 14: "Private Citizen & Property",
    15: "Religious", 16: "Telecommunication", 17: "Terrorists/Non-State Militias", 18: "Tourists",
    19: "Transportation", 20: "Unknown", 21: "Utilities", 22: "Violent Political Parties"}
    for year in years:
        success_in_target = len(data[(data['targtype1'] == target) & (data['success'] == 1) & (data['iyear'] == year)])
        success_all = len(data[(data['success'] == 1) & (data['iyear'] == year)])
        success = success_in_target / success_all * 100
        per_cent.append(success)
    # Graph generate goes here!
    chart = pygal.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=20)
    chart.title = 'Success Rate of %s from 1970 to 2016 (Except 1993) (in per cent)' %(targets[target])
    chart.x_labels = [str(x) for x in years]
    chart.add('Success Rate (%)', per_cent)
    # Export file name as Target_Success_<target_id>
    chart.render_to_file('Target_Success_%s.svg' %target)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', None)
    print("\nGraph generated!\n")
    # End of modules and return back to main
    targets_main.main(data)
