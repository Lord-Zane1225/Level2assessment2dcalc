import math
# functions


def not_blank(question):
    """Checks that a user response is not blank"""

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
            print(f"Please choose either {valid_ans_list[0]} or {valid_ans_list[1]}. ")

        elif num_of_ans == 4:
            print(f"Please choose one of {valid_ans_list[0]}, {valid_ans_list[1]}, {valid_ans_list[2]} or {valid_ans_list[3]}. ")


def num_check(question, exit_code=None):
    """Checks that users enter a float more than 0 (or optional exit code)"""

    error = "Oops - Please enter a number more than 0"

    while True:
        response = input(question).lower()

        # checks for the exit code
        if response == exit_code:
            return response
        try:
            # check response is an integer and is more than 0
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def shape_calc():
    """Gets a shape from the user and finds either the area or perimeter of that shape. """
    while True:
        is_rounded = ""
        # ask user for shape
        shape_type_chosen = string_check("Please enter what shape you would like: ", shape_tuple, 4)

        # give option to pick a different shape
        if shape_type_chosen == "triangle":
            correct_shape_ques = string_check(f"You have chosen a triangle, which can only be equilateral. Is this correct? ", yes_no_tuple, 2)
        else:
            correct_shape_ques = string_check(f"You have chosen {shape_type_chosen}. Is this correct? ", yes_no_tuple,
                                              2)

        # if yes, program continues
        if correct_shape_ques == "yes":
            # ask if user wants perimeter or area
            want_perimeter_area = string_check("Do you want the perimeter or the area? ", perimeter_area_tuple, 2)

            # find perimeter / area of square or rectangle
            if shape_type_chosen == "square" or shape_type_chosen == "rectangle":

                first_side = num_check("Please enter the length of a side")

                # if rectangle, ask for another side
                if shape_type_chosen == "rectangle":
                    second_side = num_check("Please enter the length of the other side")

                # otherwise, make second side same as first
                else:
                    second_side = first_side

                if want_perimeter_area == "perimeter":
                    perimeter = (first_side * 2) + (second_side * 2)
                    return want_perimeter_area, shape_type_chosen, perimeter, is_rounded
                else:
                    area = first_side * second_side
                    return want_perimeter_area, shape_type_chosen, area, is_rounded

            # circle finder
            elif shape_type_chosen == "circle":
                circle_radius = num_check("Please enter the radius (distance between the middle of circle to the edge): ")
                if want_perimeter_area == "perimeter":

                    # find perimeter and round to 2dp
                    perimeter_unrounded = (math.pi * 2) * circle_radius
                    perimeter = round(perimeter_unrounded, 2)
                    is_rounded = " (rounded to 2 decimal points)"

                    return want_perimeter_area, shape_type_chosen, perimeter, is_rounded
                else:

                    # find area and round to 2dp
                    unrounded_area = circle_radius * (math.pi * math.pi)
                    area = round(unrounded_area, 2)
                    is_rounded = " (rounded to 2 decimal points)"
                    return want_perimeter_area, shape_type_chosen, area, is_rounded

            # triangle finder
            else:
                triangle_base = num_check("Please enter the base of the triangle (bottom side): ")
                if want_perimeter_area == "perimeter":
                    triangle_side_one = num_check("Please enter another side of the triangle: ")
                    triangle_side_two = num_check("Please enter the remaining side pf the triangle: ")
                    perimeter = triangle_base + triangle_side_one + triangle_side_two
                    return want_perimeter_area, shape_type_chosen, perimeter, is_rounded
                else:
                    triangle_height = num_check("Please enter the height of the triangle: ")
                    area = 0.5 * triangle_base * triangle_height
                    return want_perimeter_area, shape_type_chosen, area, is_rounded






# main routine
yes_no_tuple = ("yes", "no")
shape_tuple = ("square", "rectangle", "triangle", "circle")
perimeter_area_tuple = ("perimeter", "area")

# loop for testing purposes
while True:
    user_answer = shape_calc()
    print(f"The {user_answer[0]} of your {user_answer[1]} is {user_answer[2]}{user_answer[3]}. ")
