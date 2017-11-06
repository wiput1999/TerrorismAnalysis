"""
Terrorism Analysis
"""

# Third-party libraries import
import pandas as pd
import sys

# Custom modules import
import countries_main as countries
import heatmaps_main as heatmaps
import regions_main as regions
import weapons_main as weapons
import targets_main as targets


def main():
    """ Main function use for entrypoint """
    print("Terrorism Analysis Data Visualization\n")
    menu_main()


def menu_main():
    """ Main menu function """
    print("\n*****  Main menu  *****")
    print("Which type of graph do you want to generate?")
    print("1) Weapons")
    print("2) Targets")
    print("3) Countries")
    print("4) Regions")
    print("5) Heat Maps")
    print("""Type "EXIT" to terminate program""")
    choice = input("Type number of chart which you want : ")

    if choice.lower() == "exit":
        do_exit()

    choice = int(choice)

    if choice == 1:
        menu_weapons()

    elif choice == 2:
        menu_targets()

    elif choice == 3:
        menu_countries()

    elif choice == 4:
        menu_regions()

    elif choice == 5:
        menu_heatmaps()

    else:
        print("\n***** Invalid choice! ******\n")
        menu_main()


def menu_weapons():
    """ Main menu of weapons """
    weapons.main(data)


def menu_targets():
    """ Main menu of targets """
    targets.main(data)


def menu_countries():
    """ Main menu of countries """
    countries.main(data)


def menu_regions():
    """ Main menu of regions """
    regions.main(data)


def menu_heatmaps():
    """ Main menu of heatmaps """
    heatmaps.main(data)


def do_exit():
    """ Terminate operation """
    print()
    print("************")
    print("*          *")
    print("* Goodbye! *")
    print("*          *")
    print("************")
    sys.exit(0)


# If call file directly
if __name__ == '__main__':
    # Initialize data variable as global variable name "data"
    print("Program initializing...")
    data = pd.read_csv('GTDdataset.csv', encoding='latin1', low_memory=False)
    print("Program Initialized...\n\n")
    main()
