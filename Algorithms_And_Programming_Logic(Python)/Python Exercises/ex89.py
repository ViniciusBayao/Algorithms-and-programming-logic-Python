"""
Create a program that improves the function from the previous question
so that the programmer can choose one of three edges:
    +-------=======------+ Edge 1
    ~~~~~~~~:::::::~~~~~~~ Edge 2
    <<<<<<<<------->>>>>>> Edge 3

Ex: A valid call would be a function edge receiving ("Pycharm Community", 3, 2)
~~~~~~~~:::::::~~~~~~~
 PyCharm community

 PyCharm community

 PyCharm community
~~~~~~~~:::::::~~~~~~~
"""


def edge_types():
    print("Edge 1: +-------=======------+")
    print("Edge 2: ~~~~~~~~:::::::~~~~~~~ ")
    print("Edge 3: <<<<<<<<------->>>>>>>")


def edge_choose(opt):
    if opt == 1:
        print("+-------=======------+")
        print(f"\nPycharm Community\n" * 4)
        print("+-------=======------+")
    if opt == 2:
        print("~~~~~~~~:::::::~~~~~~~")
        print(f"\nPycharm Community\n" * 4)
        print("~~~~~~~~:::::::~~~~~~~")
    if opt == 3:
        print("<<<<<<<<------->>>>>>>")
        print(f"\nPycharm Community\n" * 4)
        print("<<<<<<<<------->>>>>>>")


edge_types()

while True:
    option = int(input("Enter an option: "))

    if option >= 1:
        edge_choose(option)
    else:
        print("Invalid option! Please try again.")

    cont = input("Continue? Y or N (type using uppercase): ").upper()

    if cont == "N":
        break
