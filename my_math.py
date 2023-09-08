import math

def calculate_area(length, width):
    return length*width

def calculate_circumference(radius = 0, diameter = 0):
    pi = math.pi
    if radius == 0 and diameter == 0:
        return "Enter a number for radius or diameter..."
    elif diameter == 0 and radius > 0:
        return 2*pi*radius
    elif radius == 0 and diameter > 0:
        return 2*pi*(diameter/2)
    else:
        return "Enter only radius or diameter, not both."