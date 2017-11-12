"""
Targets modules
"""

# Third-party libraries import

# Custom modules import
import main as parent
import targets_frequency as frequency
import targets_success as success
import targets_overall as overall


def main(data):
    """ Main function with data """
    print("\n*****  Targets chart categories  *****")
    print("1) Frequency")
    print("2) Success Rate")
    print("3) Compare highest victims by target")
    print("""Type "BACK" return to main menu""")
    print("""Type "EXIT" to terminate program""")

    choice = input("Type number of chart which you want : ")

    if choice.lower() == "exit":
        parent.do_exit()
    if choice.lower() == "back":
        parent.menu_main(data)

    choice = int(choice)

    if choice == 1:
        target = get_target()
        if target == 0:
            overall.frequency(data)
        frequency.main(data, target)
    elif choice == 2:
        target = get_target()
        if target == 0:
            overall.success(data)
        success.main(data, target)
    elif choice == 3:
        overall.victims(data)
    else:
        print("\n***** Invalid choice! ******\n")
        main(data)


def get_target():
    """ Get target id """
    print("\n***** Please choose target by ID! ******")
    print("0) Overall")
    print("1) Business")
    print("2) Government (General)")
    print("3) Police")
    print("4) Military")
    print("5) Abortion Related")
    print("6) Airports & Aircraft")
    print("7) Government (Diplomatic)")
    print("8) Educational Institution")
    print("9) Food or Water Supply")
    print("10) Journalists & Media")
    print("11) Maritime (Include Ports and Maritime Facilities)")
    print("12) NGO")
    print("13) Other")
    print("14) Private Citizen & Property")
    print("15) Religious Figure/Institutions")
    print("16) Telecommunication")
    print("17) Terrorists/Non-State Militias")
    print("18) Tourists")
    print("19) Transportation (Other than aviation)")
    print("20) Unknown")
    print("21) Utilities")
    print("22) Violent Political Parties")
    target = int(input("Type number of target which you want : "))

    if target not in [x for x in range(0, 23)]:
        print("Invalid target ID!")
        get_target()

    return target

