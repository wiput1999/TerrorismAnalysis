"""
Countries modules
"""

# Third-party libraries import
import pandas as pd
import pygal

# Custom modules import
import main as parent
import countries_frequency as frequency
import countries_success as success


def main(data):
    """ Main function with data """
    print("*****  Countries chart categories  *****")
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
        country = get_country()
        frequency.main(data, country)
    elif choice == 2:
        country = get_country()
        success.main(data, country)
    else:
        print("\n***** Invalid choice! ******\n")
        main(data)


def get_country():
    """ Get country id and validate """
    country_list = [x for x in range(4, 239) if
                    x not in [9, 13, 39, 48, 52, 82, 105, 131, 133, 135, 140, 148, 150, 154, 165, 169, 170, 171, 172,
                              187, 188, 191, 193, 194, 211, 212, 224, 225, 227, 228, 232, 234, 237]] + [334, 347, 349,
                                                                                                        351, 359, 362,
                                                                                                        377, 403, 406,
                                                                                                        422, 428, 499,
                                                                                                        520, 532, 603,
                                                                                                        604, 605, 999,
                                                                                                        1001, 1002,
                                                                                                        1003, 1004]
    print("See country ID reference at https://github.com/wiput1999/TerrorismAnalysis")
    country = int(input("Type country ID to generate your chart : "))

    if country not in country_list:
        print("Invalid Country ID!")
        get_country()

    return country
