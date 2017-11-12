"""
Country success rate all year graph generator module
"""

# Third-party libraries import
import pygal as pg

# Custom modules import
import countries_main


def main(data, country, test=False):
    """ Main generate function get data and county id """
    # Graph generate goes here!
    # Export file name as Countries_Success_<country_id>

    result_x = [x for x in range(1970, 2017) if x != 1993]
    result_y = []

    for year in result_x:
        # Prevent divided by zero
        if len(data[(data['iyear'] == year) & (data['country'] == country)]) == 0:
            if test:
                return
            print("\nGraph can't generated!")
            countries_main.main(data)

        success = (len(data[(data['success'] == 1) & (data['country'] == country) & (data['iyear'] == year)]) / len(
            data[(data['iyear'] == year) & (data['country'] == country)])) * 100
        result_y.append(round(success, 2))

    # Initialize Line Chart
    chart = pg.Line(x_labels_major_count=8, show_minor_x_labels=False, truncate_legend=40, legend_at_bottom=True,
                    truncate_label=20, value_formatter=lambda x: "%.2f%%" % x)
    # Chart title
    chart.title = str(country) + ' success rate from 1970 to 2016 except 1993 (in %)'
    # X-Axis Label
    chart.x_labels = [str(x) for x in result_x]
    # Y-Axis and label
    chart.add('Success rate (%)', result_y)
    # Range of Y-Axis value
    chart.range = [0, max(result_y) + 5]
    # Save chart into file
    filename = 'Charts/Countries_Success_' + str(country) + '.svg'
    chart.render_to_file(filename)

    # End of modules and return back to main
    if test:
        return
    print("\nGraph generated!\n")
    countries_main.main(data)
