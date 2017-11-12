"""
Country frequency all year graph generator module
"""


# Third-party libraries import
import pygal as pg


# Custom modules import
import countries_main


def main(data, country, test=False):
    """ Main generate function get data and county id """
    # Graph generate goes here!
    # Export file name as Countries_Frequency_<country_id>
    # Data select condition
    result_x = [x for x in range(1970, 2017) if x != 1993]
    result_y = []

    for year in result_x:
        frequency = len(data[(data['iyear'] == year) & (data['country'] == country)])
        result_y.append(frequency)

    # Initialize Line Chart
    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True, truncate_label=20)
    # Chart title
    chart.title = 'Terriorism incidents of ' + str(country) + ' from 1970 to 2016 except 1993'
    # X-Axis Label
    chart.x_labels = [str(x) for x in result_x]
    # Y-Axis and label
    chart.add('Incidents count', result_y)

    # Save chart into file
    filename = 'Charts/Countries_Frequency_' + str(country) + '.svg'
    chart.render_to_file(filename)

    # End of modules and return back to main
    if test:
        return
    print("\nGraph generated!")
    countries_main.main(data)
