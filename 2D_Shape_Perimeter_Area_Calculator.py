import math
import pandas
import datetime


def make_statement(statement, decoration):
    """Emphasises headings by adding decorations
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def not_blank(question):
    """Checks that a user's response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def string_check(question, valid_ans_list, num_of_ans):
    """Checks that users enter the full world or the first letter of a word from a list of valid responses. """

    while True:

        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item

            elif response == item[0]:
                return item

        if num_of_ans == 2:
            print(f"Please choose either {valid_ans_list[0]} or {valid_ans_list[1]} or you can enter the first letter of either. ")

        elif num_of_ans == 4:
            print(f"Please choose one of {valid_ans_list[0]}, {valid_ans_list[1]}, {valid_ans_list[2]} or {valid_ans_list[3]} or you can enter the first letter of any. ")


def num_check(question, minimum, exit_code=None):
    """Checks if user's input is a number (float) and is above another number"""
    error = f"Please enter a number that is greater than {minimum}. "
    # get user answer
    response = input(question)
    if response == exit_code:
        return response
    while True:
        try:
            response = int(response)
            # if correct return response
            if response > minimum:
                return response
            else:
                # if below minimum print error
                print(error)
        # if not a number print error
        except ValueError:
            print(error)


def shape_calc():
    """Gets a shape from the user and finds either the area or perimeter of that shape. """
    while True:
        is_rounded = ""

        # ask user for shape
        shape_type_chosen = string_check("Please enter what shape you would like: ", shape_tuple, 4)

        # ask if user wants perimeter or area
        want_perimeter_area = string_check("Do you want the perimeter or the area? ", perimeter_area_tuple, 2)

        # find perimeter / area of square or rectangle
        if shape_type_chosen == "square" or shape_type_chosen == "rectangle":

            while True:
                # ask user for the length of a side
                first_side = num_check("Please enter the length of a side", 0, "x")
                if first_side > 1000:
                    break
                else:
                    continue

            # if rectangle, ask for another side
            if shape_type_chosen == "rectangle":
                second_side = num_check("Please enter the length of the other side", 0, "x")

            # otherwise, make second side same as first
            else:
                second_side = first_side

            # find perimeter and area
            try:
                perimeter = (first_side * 2) + (second_side * 2)
                area = first_side * second_side
                return want_perimeter_area, shape_type_chosen, perimeter, area, is_rounded
            # tell user that they have not given enough information for this calculation
            except ValueError:
                print("You have not given enough information to calculate either the perimeter or area. Please try again.")
                return "fail"

        # circle finder
        elif shape_type_chosen == "circle":
            circle_radius = num_check("Please enter the radius (distance between the middle of circle to the edge): ", 0, "x")
            try:
                # find perimeter and round to 2dp
                perimeter_unrounded = (math.pi * 2) * circle_radius
                perimeter = round(perimeter_unrounded, 2)

                # find area and round to 2dp
                unrounded_area = circle_radius * (math.pi * math.pi)
                area = round(unrounded_area, 2)
                is_rounded = " (rounded to 2 decimal points)"
                # return results
                return want_perimeter_area, shape_type_chosen, perimeter, area, is_rounded
            except ValueError:
                print("You have not given enough information to calculate either the perimeter or area. Please try again.")
                return "fail"

        # triangle finder
        else:
            if want_perimeter_area == "area":
                # ask user for the height if they want area
                triangle_height = num_check("Please enter the height of the triangle: ", 0, "x")
            else:
                triangle_height = ""

            triangle_base = num_check("Please enter the base of the triangle (bottom side): ", 0, "x")

            triangle_side_one = num_check("Please enter another side of the triangle: ", 0, "x")
            triangle_side_two = num_check("Please enter the remaining side of the triangle: ", 0, "x")
            try:
                if triangle_side_one == "x" or triangle_side_two == "x":
                    perimeter = "N/A"
                else:
                    perimeter = triangle_base + triangle_side_one + triangle_side_two
                if triangle_height == "":
                    area = "N/A"
                else:
                    area = 0.5 * triangle_base * triangle_height
                return want_perimeter_area, shape_type_chosen, perimeter, area, is_rounded
            except ValueError:
                print("You have not given enough information to calculate either the perimeter or area. Please try again.")
                return "fail"


def instructions():
    """Displays the instructions for the program."""
    print(make_statement("Instructions", "ℹ️"))

    print('''
For each 2D shape enter: 
- A name to identify the shape
- The type of shape (we have squares, rectangles, triangles and circles)
- Whether you want either area or perimeter
- The requested parts of the shape (sides, radius, height) 
    (you can also put <x> if you don't have the requested feature)


The program will record all user inputs and calculate the 
perimeter and area (if possible, some cases will not have both available).

Once you have entered all the shapes you wish to calculate, input the 
exit code ('complete'), and the program will display the shape's
information and write the data to a dated text file. 
    ''')


# main routine
# tuples for different options
yes_no_tuple = ("yes", "no")
shape_tuple = ("square", "rectangle", "triangle", "circle")
perimeter_area_tuple = ("perimeter", "area")

# pandas lists
all_names = []
all_sides = []
all_areas = []
all_perimeters = []

# dictionary
shapes_dict = {
    'Name': all_names,
    'Shape Features': all_sides,
    'Area': all_areas,
    'Perimeter': all_perimeters,
}

# main heading
print(make_statement("2D Shape Perimeter Area Calculator", "--"))
print()

# ask user if they want to see the instructions
want_instructions = string_check("Would you like to read the instructions? ", yes_no_tuple, 2)
if want_instructions == "yes":
    instructions()
print()

# loop so user can enter as many shapes as they wish
while True:
    # get name of the shape
    name = not_blank("Please enter the question name / something to identify your shape by, or enter 'complete' if you have finished: ")
    # if user is done calculating, break the loop
    if name == "complete":
        break

    # get the perimeter / area of the shapes
    user_answer = shape_calc()

    # if the user didn't enter enough information, try again.
    if user_answer == "fail":
        continue







print("finish")





