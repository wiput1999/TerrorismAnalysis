"""
Regions frequency all year graph generator module
"""

# Third-party libraries import
import pygal as pg

# Custom modules import
import regions_main


def main(data, region, test=False):
    """ Main generate function get data and region id """
    # Graph generate goes here!
    # Export file name as Regions_Frequency_<region_id>

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

    result_x = [x for x in range(1970, 2017) if x != 1993]
    result_y = []

    for year in result_x:
        frequency = len(data[(data['iyear'] == year) & (data['region'] == region)])
        result_y.append(frequency)

    # Initialize Line Chart
    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True,
                    truncate_label=20)
    # Chart title
    chart.title = 'Terriorism incidents of ' + regions[region] + ' from 1970 to 2016 except 1993'
    # X-Axis Label
    chart.x_labels = [str(x) for x in result_x]
    # Y-Axis and label
    chart.add('Incidents count', result_y)

    # Save chart into file
    filename = 'Charts/Regions_Frequency_' + regions[region] + '.svg'
    chart.render_to_file(filename)

    # End of modules and return back to main
    if test:
        return
    print("\nGraph generated!")
    regions_main.main(data)
