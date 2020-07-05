from math import pi

# To do
# Ask user for shape
# Ask user for dimensions
# Calculate using shape formula
# Print area

# Check response function
def check(question, error, shape_check):
    valid = False
    while not valid:
        try:
            # If shape_check == "yes", Then the program is looking for a shape.
            if shape_check == "yes":
                response = int(input(question))
                if response <= 0 or response > 5:
                    print("Please enter a number between 1 and 5.")
                    continue
                # If all values are valid then return response.
                else:
                    return response
            # Otherwise, program is looking for dimensions. (Line 14)
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
                x = check("Enter Side Dimension: ", "Please enter a valid number", "no")
                answer = x*x
                return round(answer, 2)
            # Rectangle
            elif shape == 2:
                x = check("Enter Length: ", "Please enter a valid number", "no")
                y = check("Enter Width: ", "Please enter a valid number", "no")
                answer = x*y
                return round(answer, 2)
            # Circle
            elif shape == 3:
                x = check("Enter radius: ", "Please enter a valid number", "no")
                answer = pi*x*x
                return round(answer, 2)
            # Triangle
            elif shape == 4:
                x = check("Enter base: ", "Please enter a valid number", "no")
                y = check("Enter height: ", "Please enter a valid number", "no")
                answer = (y*x)/2
                return round(answer, 2)
            # Parallelogram
            elif shape == 5:
                x = check("Enter base: ", "Please enter a valid number", "no")
                y = check("Enter Height: ", "Please enter a valid number", "no")
                answer = x*y
                return round(answer, 2)

        except ValueError:
            print("Enter a valid number.")
            continue


# Main routine
shape = check("1)Square 2)Rectangle 3)Circle 4)Triangle 5)Parallelogram ", "Please enter a valid number.", "yes")

shape_list = ["Square", "Rectangle", "Circle", "Triangle", "Parallelogram"]

# This loop saves me 5 if statements by checking if shape == i, otherwise i += 1.
i = 0
valid = False
while not valid:
    if shape == i:
        shape = shape_list[i-1]
        break
    else:
        i += 1

# Getting shape from i (line 80)
dimensions = calculate(i)
print("{} area is {}".format(shape, dimensions))

