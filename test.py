"""
Test modules
"""
# Import modules
import countries_frequency
import countries_success
import regions_overall
import regions_success
import regions_frequency
import targets_overall
import targets_success
import targets_frequency
import weapons_overall
import weapons_success
import weapons_frequency
import pandas as pd


def main():
    """ Main function """
    # Initialize data variable as global variable name "data"
    print("Program initializing...")
    data = pd.read_csv('GTDdataset.csv', encoding='latin1', low_memory=False)
    print("Program Initialized...\n\n")

    print("********** All test begin **********")

    # Countries graph test
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
    for i in country_list:
        countries_success.main(data, i, True)
        print("********** Country %d success passed **********" % i)
        countries_frequency.main(data, i, True)
        print("********** Country %d frequency passed **********" % i)

    print("********** All countries test passed **********")

    # Region overall test
    regions_overall.success(data, True)
    regions_overall.frequency(data, True)

    print("********** Overall regions test passed **********")

    # Regions test
    for i in range(1, 13):
        regions_success.main(data, i, True)
        print("********** Region %d success passed **********" % i)
        regions_frequency.main(data, i, True)
        print("********** Region %d frequency passed **********" % i)

    print("********** All regions test passed **********")

    # Targets overall test
    targets_overall.frequency(data, True)
    targets_overall.success(data, True)

    print("********** Overall targets test passed **********")

    # Targets test
    for i in range(1, 23):
        targets_success.main(data, i, True)
        print("********** Target %d success passed **********" % i)
        targets_frequency.main(data, i, True)
        print("********** Target %d frequency passed **********" % i)

    print("********** All targets test passed **********")

    # Weapon overall test
    weapons_overall.frequency(data, True)
    weapons_overall.success(data, True)

    print("********** Overall weapons test passed **********")

    # Weapon test
    for i in range(1, 14):
        weapons_frequency.main(data, i, True)
        print("********** Weapon %d success passed **********" % i)
        weapons_success.main(data, i, True)
        print("********** Weapon %d frequency passed **********" % i)

    print("********** All weapons test passed **********")
    print("********** All tests passed **********")


if __name__ == '__main__':
    main()
