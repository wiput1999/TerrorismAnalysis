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
    # Graph generate goes here!
    # Export file name as Target_Success_<target_id>

    # End of modules and return back to main
    print("\nGraph generated!\n")
    targets_main.main(data)
