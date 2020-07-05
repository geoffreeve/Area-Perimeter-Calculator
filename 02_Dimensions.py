# To do
# Ask user for shape dimensions
# print shape dimensions

def calculate():
    valid = False
    while not valid:
        try:
            response = float(input("Enter dimensions: "))
            # If response equals or is lower than 0, print error.
            if response <= 0:
                print("Please enter a number higher than 0")
                continue
            # If user input is valid, return response
            else:
                return response
        except ValueError:
            print("Enter a valid number.")
            continue


# Main routine
dimensions = calculate()
print(dimensions)
