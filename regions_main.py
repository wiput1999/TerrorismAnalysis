"""
Regions modules
"""

# Third-party libraries import
import pandas as pd
import pygal

# Custom modules import
import main as parent
import regions_frequency as frequency
import regions_success as success
import regions_overall as overall


def main(data):
    """ Main function with data """
    print("\n*****  Regions chart categories  *****")
    print("1) Frequency")
    print("2) Success Rate")
    print("""Type "BACK" return to main menu""")
    print("""Type "EXIT" to terminate program""")

    choice = input("Type number of chart which you want : ")

    if choice.lower() == "exit":
        parent.do_exit()
    if choice.lower() == "back":
        parent.menu_main()

    choice = int(choice)

    if choice == 1:
        region = get_region()
        if region == 0:
            overall.frequency(data)
        frequency.main(data, region)
    elif choice == 2:
        region = get_region()
        if region == 0:
            overall.success(data)
        success.main(data, region)
    else:
        print("\n***** Invalid choice! ******\n")
        main(data)


def get_region():
    """ Get region id """
    print("\n***** Please choose region by ID! ******")
    print("0) Overall")
    print("1) North America")
    print("2) Central America & Caribbean")
    print("3) South America")
    print("4) East Asia")
    print("5) Southeast Asia")
    print("6) South Asia")
    print("7) Central Asia")
    print("8) Western Europe")
    print("9) Eastern Europe")
    print("10) Middle East & North Africa")
    print("11) Sub-Saharan Africa")
    print("12) Australasia & Oceania")
    region = int(input("Type number of region which you want : "))

    if region not in [x for x in range(0, 13)]:
        print("Invalid region ID!")
        get_region()

    return region
