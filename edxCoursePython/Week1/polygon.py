import math


def polygon_calculate_perimeter(polygon_number_of_sides, polygon_side_length):
    """ returns perimeter of a polygon
    :param polygon_number_of_sides: Number of sides of a polygon
    :param polygon_side_length: Length of a single side of a polygon
    :return: Returns the Perimeter of a polygon
    """
    return polygon_number_of_sides * polygon_side_length


def polygon_calculate_area(polygon_number_of_sides, polygon_side_length):
    """
    :param polygon_number_of_sides: Number of sides of a polygon
    :param polygon_side_length: Length of a single side of a polygon
    :return: Returns the Area of a polygon
    """
    return (0.25 * polygon_number_of_sides * (polygon_side_length ** 2)) / math.tan(math.pi / polygon_number_of_sides)


def polygon_calculate_sum(polygon_number_of_sides, polygon_side_length, rounding=4):
    """
    :param polygon_number_of_sides: Number of sides of a polygon
    :param polygon_side_length: Length of a single side of a polygon
    :param rounding - default 4, optional parameter for how many numbers after the decimal point we will to round to
    :return: Returns the Sum of Area plus squared Perimeter of a polygon
    """
    return round(polygon_calculate_area(polygon_number_of_sides, polygon_side_length) + polygon_calculate_perimeter(
        polygon_number_of_sides, polygon_side_length) ** 2, rounding)