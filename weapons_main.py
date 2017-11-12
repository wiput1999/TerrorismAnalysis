"""
Weapons modules
"""

# Third-party libraries import
import pandas as pd
import pygal

# Custom modules import
import main as parent
import weapons_frequency as frequency
import weapons_success as success
import weapons_overall as overall


def main(data):
    """ Main function with data """
    print("*****  Weapons chart categories  *****")
    print("1) Frequency")
    print("2) Success Rate")
    print("""Type "BACK" return to main menu""")
    print("""Type "EXIT" to terminate program""")

    choice = input("Type number of chart which you want : ")

    if choice.lower() == "exit":
        parent.do_exit()
    if choice.lower() == "back":
        parent.menu_main(data)

    choice = int(choice)

    if choice == 1:
        weapon = get_weapon()
        if weapon == 0:
            overall.frequency(data)
        frequency.main(data, weapon)
    elif choice == 2:
        weapon = get_weapon()
        if weapon == 0:
            overall.success(data)
        success.main(data, weapon)
    else:
        print("\n***** Invalid choice! ******\n")
        main(data)


def get_weapon():
    """ Get weapon id """
    print("\n***** Please choose weapon by ID! ******")
    print("0) Overall")
    print("1) Biological")
    print("2) Chemical")
    print("3) Radiological")
    print("4) Nuclear")
    print("5) Firearms")
    print("6) Explosives/Bombs/Dynamites")
    print("7) Fake Weapons")
    print("8) Incendiary")
    print("9) Melee")
    print("10) Vehicle")
    print("11) Sabotage Equipment")
    print("12) Other")
    print("13) Unknown")
    weapon = int(input("Type number of weapon which you want : "))

    if weapon not in [x for x in range(0, 13)]:
        print("Invalid weapon ID!")
        get_weapon()

    return weapon

