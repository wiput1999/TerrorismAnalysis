"""
Regions frequency all year graph generator module
"""


# Third-party libraries import
import pandas as pd
import pygal


# Custom modules import
import regions_main


def main(data, region):
    """ Main generate function get data and region id """
    # Graph generate goes here!
    # Export file name as Regions_Frequency_<region_id>

    # End of modules and return back to main
    print("\nGraph generated!\n")
    regions_main.main(data)
