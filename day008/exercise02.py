# Paint Area Calculator

wall_height = int(input("What is the height of the wall? : "))
wall_width = int(input("What is the width of the wall? : "))
coverage = 5


def wall_area_calc(height, width, coverage):
    area = height * width
    number_of_cans = round(area / coverage)
    print(f"You need {number_of_cans} cans of paint")


wall_area_calc(height=wall_height, width=wall_width, coverage=coverage)

# Can also define in TWO ways:
# wall_area_calc(wall_width=wall_width, wall_height=wall_height, coverage=coverage)
# wall_area_calc(wall_height, wall_width, coverage)
