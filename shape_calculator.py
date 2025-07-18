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
            print(f"Please choose either {valid_ans_list[0]} or {valid_ans_list[1]} or you can enter the first letter of either. ")

        elif num_of_ans == 4:
            print(f"Please choose one of {valid_ans_list[0]}, {valid_ans_list[1]}, {valid_ans_list[2]} or {valid_ans_list[3]} or you can enter the first letter of any. ")


def num_check(question, minimum, exit_code):
    """Checks if user's input is a number and is above another number"""
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

        # give option to pick a different shape
        correct_shape_ques = string_check(f"You have chosen {shape_type_chosen}. Is this correct? ", yes_no_tuple, 2)

        # if yes, program continues
        if correct_shape_ques == "yes":
            # ask if user wants perimeter or area
            want_perimeter_area = string_check("Do you want the perimeter or the area? ", perimeter_area_tuple, 2)

            # find perimeter / area of square or rectangle
            if shape_type_chosen == "square" or shape_type_chosen == "rectangle":

                first_side = num_check("Please enter the length of a side", 0, "x")

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


# main routine
yes_no_tuple = ("yes", "no")
shape_tuple = ("square", "rectangle", "triangle", "circle")
perimeter_area_tuple = ("perimeter", "area")

# loop for testing purposes
print("if you do not have the number for one of the entries, please input <x>")
while True:
    user_answer = shape_calc()
    # if failed, print nothing and restart loop
    if user_answer[0] == "area":
        print(f"The area of your {user_answer[1]} is {user_answer[3]}{user_answer[4]} (perimeter is {user_answer[2]}).")
    elif user_answer[0] == "perimeter":
        print(f"The perimeter of your {user_answer[1]} is {user_answer[2]}{user_answer[4]} (area is {user_answer[3]}).")
    else:
        continue
