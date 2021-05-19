import math


def convert_to(number, to="radians"):
    """
    :param number: number to convert
    :param to: end unit of measure. default = 'radians'. Alternative = 'degrees'
    :return: converted number
    """
    if to == "degrees":
        print("--------------- degrees to radians: deg * 180 / pi")
        return math.degrees(number)
    print("--------------- degrees to radians: deg / 180 * pi")
    return math.radians(number)


def get_angle_from_ratio(number, ratio="cosine", result_in_degrees=True):
    if ratio == "cosine":
        angle = math.acos(number)
    elif ratio == "sine":
        angle = math.asin(number)
    elif ratio == "tangent":
        return math.tan(number)

    if result_in_degrees:
        return math.degrees(angle)


# print(get_angle_from_ratio(number=1/6, ratio="sine"))

# print(convert_to(number=2.5, to="degrees"))

print(math.cos(math.radians(9.594068226860461)))