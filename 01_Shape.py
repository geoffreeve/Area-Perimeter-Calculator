# To do
# Ask user for shape
# Print shape

# Check response function
def check(question, error, shape_check):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            # If shape_check == "yes", Then the program is looking for a shape.
            if shape_check == "yes":
                if response <= 0 or response > 5:
                    print("Please enter a number between 1 and 5.")
                    continue
                # If all values are valid then return response.
                else:
                    return response
        # If invalid values are caught, like strings, then print an error and continue.
        except ValueError:
            print(error)
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

# Print selected shape
print(shape)
