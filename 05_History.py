from math import pi

# To do
# Ask user for shape
# Ask user for dimensions
# Calculate using shape formula
# Print area
# Store all calculations in history and print when user ends the program.

# Check response function
def check(question, error, shape_check, cont):
    valid = False
    while not valid:
        try:
            # If cont == "yes" then it is checking if user wants to continue or not.
            if cont == "yes":
                response = int(input(question))
                # If number is lower than 1 or higher than 2 then print error
                if response < 1 or response > 2:
                    print(error)
                    continue
                else:
                    return response
            # If shape_check == "yes", Then the program is looking for a shape.
            elif shape_check == "yes":
                response = int(input(question))
                # If response is lower than 0 or higher than 5, print error.
                if response <= 0 or response > 5:

                    print("Please enter a number between 1 and 5.")
                # If all values are valid then return response.
                else:
                    return response
            # Otherwise, program is looking for dimensions. (Line 24)
            else:
                response = float(input(question))

                if response <= 0:
                    print("Please enter a number higher than 0.")
                # If all values are valid then return response.
                else:
                    return response
        # If invalid values are caught, like strings, then print an error and continue.
        except ValueError:
            print(error)
            continue

# Calculates dimensions
def calculate(shape):
    valid = False
    while not valid:
        try:
            # Square
            if shape == 1:
                s = check("Enter Side Dimension: ", "Please enter a valid number", "no", "no")
                answer = s*s
                return round(answer, 2)
            # Rectangle
            elif shape == 2:
                l = check("Enter Length: ", "Please enter a valid number", "no", "no")
                w = check("Enter Width: ", "Please enter a valid number", "no", "no")
                answer = w*l
                return round(answer, 2)
            # Circle
            elif shape == 3:
                r = check("Enter radius: ", "Please enter a valid number", "no", "no")
                answer = pi*r*r
                return round(answer, 2)
            # Triangle
            elif shape == 4:
                b = check("Enter base: ", "Please enter a valid number", "no", "no")
                h = check("Enter height: ", "Please enter a valid number", "no", "no")
                answer = (h*b)/2
                return round(answer, 2)
            # Parallelogram
            elif shape == 5:
                x = check("Enter base: ", "Please enter a valid number", "no", "no")
                y = check("Enter Height: ", "Please enter a valid number", "no", "no")
                answer = x*y
                return round(answer, 2)
        except ValueError:
            print("Enter a valid number.")
            continue


# Main routine
# Variables and arrays being declared ahead.
a = 0
b = 0
shape_arr = []
area_arr = []

valid = False
while not valid:
    # Gets shape
    shape = check("\n1)Square 2)Rectangle 3)Circle 4)Triangle 5)Parallelogram ", "Please enter a valid number.", "yes", "no")

    shape_list = ["Square", "Rectangle", "Circle", "Triangle", "Parallelogram"]
    i = 0
    while not valid:
        # This loop saves me 5 if statements by checking if shape == i, otherwise i += 1.
        if shape == i:
            shape = shape_list[i-1]
            break
        else:
            i += 1
            continue

    # Getting dimensions using shape formula. Shape is i.
    dimensions = calculate(i)
    # Prints shape and calculated area.
    print("{} area is {}".format(shape, dimensions))
    # Asking user if they want to continue or not
    cont = check("\nDo you want to continue? Enter 1 to continue or 2 to exit", "\nPlease enter 1 to continue or 2 to exit", "no", "yes")
    # History here
    # The shape and array are added to their separate arrays where they are later printed.
    shape_arr.append(shape)
    area_arr.append(dimensions)
    a += 1

    # This checks cont from earlier (line 111)
    # If cont == 1 then continue
    if cont == 1:
        continue
    # Else print history and end program.
    else:
        print("\nHistory -")
        while b != len(shape_arr):
            print("{} area is {}".format(shape_arr[b], area_arr[b]))
            b += 1
            continue
        quit()
