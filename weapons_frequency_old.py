"""
Weapons frequency all year graph generator module
"""


# Third-party libraries import
import pandas as pd
import pygal


# Custom modules import
import weapons_main


def main(data, weapon):
    """ Main generate function get data and weapon id """
    # Graph generate goes here!
    # Export file name as Weapons_Frequency_<weapon_id>

    # End of modules and return back to main
    print("\nGraph generated!\n")
    weapons_main.main(data)
