from math import pi


# check function
def check(question, num, cont):
    shape_list = ["circle", "square", "rectangle", "rhombus", "parallelogram"]

    valid = False
    while not valid:
        try:
            # If num == "yes" then program is looking for a number
            if num == "yes":
                response = float(input(question))
                if response == "":
                    print("Please enter a valid number.")
                    continue
                elif response <= 0:
                    print("Please enter a number higher than 0.")
                    continue
                return response
            # If cont == "yes" then program is asking if the user wants to continue or not.
            if cont == "yes":
                response = int(input(question))
                if response == "":
                    "Please enter 1 to continue or 2 to exit."
                elif response < 1 or response > 2:
                    "Please enter 1 to continue or 2 to exit."
                return response
            # If num and cont == "no" then program is looking for a string
            else:
                # Checks for shape or first letter of shape.
                response = input(question).lower()
                # Checks if response is a valid shape, then returns response
                for item in shape_list:
                    if response == item:
                        return response

                print("\nPlease enter a valid shape.\n")
        # If program catches value error, then print error and continue
        except ValueError:
            print("Please enter a valid response.")
            continue


# calculate function
def calculate(shape, cont, shape_arr=[], area_arr=[], perimeter_arr=[]):
    # History array holds other arrays which store the shape, area and perimeter data.
    history = [shape_arr, area_arr, perimeter_arr]

    # If cont == "yes" Then print history, then exit.
    if cont == "yes":
        i = 0
        print("\n----------------")
        print("History -")
        print("----------------")
        while i < len(history[0]):
            print("{} Area = {:.2f}".format(history[0][i], history[1][i]))
            print("{} Perimeter = {:.2f}".format(history[0][i], history[2][i]))
            print("----------------")
            i += 1
        input()
        exit()
    if shape == "square":
        side_1 = check("\nEnter first Square Side: ", "yes", "no")
        area = side_1 * side_1
        perimeter = side_1 * 4

    if shape == "circle":
        radius = check("\nEnter Circle Radius:  ", "yes", "no")
        area = pi * radius * radius
        perimeter = 2 * pi * radius

    if shape == "rectangle":
        side_1 = check("\nEnter first Rectangle side: ", "yes", "no")
        side_2 = check("Enter second Rectangle side: ", "yes", "no")
        area = side_1 * side_2
        perimeter = side_1 * 2 + side_2 * 2

    if shape == "rhombus":
        diagonal_1 = check("\nEnter first Rhombus Diagonal: ", "yes", "no")
        diagonal_2 = check("Enter second Rhombus Diagonal: ", "yes", "no")
        area = (diagonal_1 * diagonal_2) / 2
        perimeter = (4 * diagonal_1)

    if shape == "parallelogram":
        base = check("\nEnter Parallelogram base: ", "yes", "no")
        side = check("Enter Parallelogram side: ", "yes", "no")
        area = (base * side)
        perimeter = (2 * (side + base))

    # Prints Shape, Area and Perimeter at the end of calculation
    # Then values append into history lists.
    print("\n{} area is {:.2f}".format(shape, area))
    print("{} perimeter is {:.2f}\n".format(shape, perimeter))
    history[0].append(shape)
    history[1].append(area)
    history[2].append(perimeter)


# Main routine
print("!!!!!!!!!!!!!")
print("Welcome to Area/Perimeter Calculator")
print("To use, enter a shape and then the dimensions.")
print("When you are done, history of previous calculations will print on screen.")
print("!!!!!!!!!!!!!\n")
valid = False
while not valid:
    # Asking user to select a shape
    
    print("Shapes - Circle, Rectangle, Square, Rhombus, Parallelogram\n")
    shape = check("Select a shape. ", "no", "no")
    # Taking that shape and asking for units, then printing area & perimeter.
    calculate(shape, "no")
    # After printing calculations, ask user if they want to continue or not
    # If not then print history in calculate function.
    cont = check("Enter any number to continue or 2 to exit ", "no", "yes")
    if cont == 2:
        calculate(shape, "yes")
