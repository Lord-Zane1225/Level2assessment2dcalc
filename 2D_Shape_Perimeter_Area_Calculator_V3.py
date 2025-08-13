import math
import pandas
from datetime import date


def make_statement(statement, decoration):
    """Emphasises headings by adding decorations
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def not_blank(question):
    """Checks that a user's response is not blank"""

    while True:
        # ask question get response
        response = input(question)

        # if response isn't blank, return it
        if response != "":
            return response

        # otherwise, print error
        print("Sorry, this can't be blank. Please try again. \n")


def string_check(question, valid_ans_list, num_of_ans):
    """Checks that users enter the full world or the first letter of a word from a list of valid responses. """

    while True:

        # ask user question and get response
        response = input(question).lower()

        # check if the user's response is inside the list of valid answers
        for str_item in valid_ans_list:
            if response == str_item:
                return str_item
            # check if the user's response is the first letter of a valid answer
            elif response == str_item[0]:
                return str_item

        # changes the error message depending on how large the answer list is for aesthetics.
        if num_of_ans == 2:
            print(f"Please choose either {valid_ans_list[0]} or {valid_ans_list[1]} or you can enter the first letter of either. ")

        elif num_of_ans == 4:
            print(f"Please choose one of {valid_ans_list[0]}, {valid_ans_list[1]}, {valid_ans_list[2]} or {valid_ans_list[3]} or you can enter the first letter of any. ")


def num_check(question, minimum):
    """Checks if user's input is a number (float) and is above another number"""
    error = f"Please enter a number that is greater than {minimum}. "
    while True:
        # get user answer
        response = input(question)

        # float checker
        try:
            # check if the response is a float
            response = float(response)

            # if correct return response
            if response > minimum:
                return response
            else:
                # if below minimum print error
                print(error)

        # if not a float print error
        except ValueError:
            print(error)


def instructions():
    """Displays the instructions for the program."""
    print(make_statement("Instructions", "ℹ️"))

    print('''
For each 2D shape enter: 
- A name to identify the shape
- The type of shape (we have squares, rectangles, triangles and circles)
- Whether you want either area or perimeter
- The requested parts of the shape (sides, radius, height). 

The program will record all user inputs and calculate the 
perimeter and area (if possible, some cases will not have both available).

Once you have entered all the shapes you wish to calculate, input the 
exit code ('complete'), and the program will display the shape's
information and write the data to a dated text file. 
    ''')


def shape_calc():
    """Gets a shape from the user and finds either the area or perimeter of that shape. """

    # ask user for shape
    shape_type_chosen = string_check("Please enter what shape you would like: ", shape_tuple, 4)

    # ask if user wants perimeter or area
    want_perimeter_area = string_check("Do you want the perimeter or the area? ", perimeter_area_tuple, 2)

    # variable to reduce repeated code
    answer_printing = f"The {want_perimeter_area} of your {shape_type_chosen} is "

    # find perimeter / area of square or rectangle
    if shape_type_chosen == "square" or shape_type_chosen == "rectangle":

        # ask user for the length of a side
        first_side = num_check("Please enter the length of a side: ", 0)

        # if rectangle, ask for another side
        if shape_type_chosen == "rectangle":
            second_side = num_check("Please enter the length of the other side: ", 0)

        # otherwise, make second side same as first
        else:
            second_side = first_side

        if want_perimeter_area == "perimeter":
            # find perimeter
            perimeter = round(first_side + first_side + second_side + second_side, 2)
            print(answer_printing, perimeter)

            # append results
            all_shapes.append(shape_type_chosen)
            all_areas_perimeters.append(f"{perimeter}")
            all_wanted.append(want_perimeter_area)
            all_sides.append(f"{first_side}s1, {second_side}s2")
            return shape_type_chosen
        else:
            # find area
            area = round(first_side * second_side, 2)
            print(answer_printing, area)

            # append results
            all_shapes.append(shape_type_chosen)
            all_areas_perimeters.append(f"{area}")
            all_wanted.append(want_perimeter_area)
            all_sides.append(f"{first_side}s1, {second_side}s2")
            return shape_type_chosen


    # circle finder
    elif shape_type_chosen == "circle":
        circle_radius = num_check("Please enter the radius (distance between the middle of circle to it's edge): ", 0)

        if want_perimeter_area == "perimeter":
            # find perimeter and round to 2dp
            perimeter = round((math.pi * 2) * circle_radius, 2)
            print(answer_printing, perimeter)

            # append results
            all_shapes.append(shape_type_chosen)
            all_areas_perimeters.append(f"{perimeter}")
            all_wanted.append(want_perimeter_area)
            all_sides.append(f"{circle_radius}r")
            return shape_type_chosen

        else:
            # find area and round to 2dp
            area = round(circle_radius * (math.pi * math.pi), 2)
            print(answer_printing, area)

            # append results
            all_shapes.append(shape_type_chosen)
            all_areas_perimeters.append(f"{area}")
            all_wanted.append(want_perimeter_area)
            all_sides.append(f"{circle_radius}r")
            return shape_type_chosen


    # triangle finder
    else:

        # if the user wants the area, calc area
        if want_perimeter_area == "area":
            # ask user for the height
            triangle_height = num_check("Please enter the height of the triangle: ", 0)
            # ask user for the base side length
            triangle_base = num_check("Please enter the base of the triangle (bottom side): ", 0)

            # find area
            unrounded_area = 0.5 * triangle_base * triangle_height
            area = round(unrounded_area, 2)

            # print the answer
            print(answer_printing, area)

            # append results
            all_shapes.append(shape_type_chosen)
            all_areas_perimeters.append(f"{area}")
            all_wanted.append(want_perimeter_area)
            all_sides.append(f"{triangle_height}h, {triangle_base}b")
            return shape_type_chosen

        # if the user wants the perimeter, calc perimeter
        else:
            # ask user for the side lengths
            triangle_base = num_check("Please enter a side of the triangle: ", 0)
            triangle_side_one = num_check("Please enter another side of the triangle: ", 0)
            triangle_side_two = num_check("Please enter the remaining side of the triangle: ", 0)

            # find perimeter
            perimeter = round(triangle_base + triangle_side_one + triangle_side_two, 2)

            # print the answer
            print(answer_printing, perimeter)

            # append results
            all_shapes.append(shape_type_chosen)
            all_areas_perimeters.append(f"{perimeter}")
            all_wanted.append(want_perimeter_area)
            all_sides.append(f"{triangle_base}s1, {triangle_side_one}s2, {triangle_side_two}s3")
            return shape_type_chosen



# main routine
# tuples for different options
yes_no_tuple = ("yes", "no")
shape_tuple = ("square", "rectangle", "triangle", "circle")
perimeter_area_tuple = ("perimeter", "area")

# pandas lists
all_names = []
all_shapes = []

all_areas_perimeters = []
all_sides = []
all_wanted = []

# dictionary
shapes_dict = {
    'Name': all_names,
    'Shape': all_shapes,
    'Features': all_sides,
    'Results (2dp)': all_areas_perimeters,
    'Requested': all_wanted
}

# main heading
print(make_statement("2D Shape Perimeter and Area Calculator", "--"))
print()

# ask user if they want to see the instructions
want_instructions =                                                                                         string_check("Would you like to read the instructions? ", yes_no_tuple, 2)
if want_instructions == "yes":
    instructions()
print()

# loop so user can enter as many shapes as they wish
while True:
    # get name of the shape
    print()
    name = not_blank("Please enter the question name / something to identify your shape by, or enter 'complete' if you have finished: ")
    # if user is done calculating, break the loop
    if name == "complete":
        break

    # get the perimeter / area of the shapes
    user_answer = shape_calc()

    # if the user didn't enter enough information, try again.
    if user_answer == "fail":
        continue

    # otherwise, append the name
    else:
        all_names.append(name)

# create dataframe / table from directory
shapes_frame = pandas.DataFrame(shapes_dict)

# remove first collum
shape_calc_string = shapes_frame.to_string(index=False)

# get current date for heading and filename
today = date.today()

# get day month and year as separate strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# get heading of results
heading_string = make_statement(f"2D Shape Perimeter Area Calculator Results ({day} / {month} / {year})", "-")


# set up list for what should be printed and written to file
to_write = [heading_string, "\n",
    shape_calc_string, "\n",]

# print results
print()
for item in to_write:
    print(item)

# create file to hold data (add txt extension)
file_name = f"2d_shape_calc_results_{day}_{month}_{year}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")


# write the items to the file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")


