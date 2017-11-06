"""
Country success rate all year graph generator module
"""


# Third-party libraries import
import pandas as pd
import pygal


# Custom modules import
import countries_main


def main(data, country):
    """ Main generate function get data and county id """
    # Graph generate goes here!
    # Export file name as Countries_Success_<country_id>

    # End of modules and return back to main
    print("\nGraph generated!\n")
    countries_main.main(data)
