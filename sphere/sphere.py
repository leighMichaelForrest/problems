import math
import sys

PI = math.pi

def diameter(radius):
    try:
        radius = float(radius)
        return radius * 2
    except ValueError:
        return 0

def circumference(radius):
    try:
        return PI * diameter(radius)
    except ValueError:
        return 0

def surface_area(radius):
    try:
        radius = float(radius)
        return 4 * PI * (radius**2)
    except ValueError:
        return 0

def volume(radius):
    try:
        radius = float(radius)
        return (surface_area(radius) * radius) / 3
    except ValueError:
        return 0


if __name__ == '__main__':
    try:
        radius = sys.argv[1]
    except IndexError:
        radius = 0

    print("The radius is", radius)
    print("The diameter is", diameter(radius))
    print("The circumference is", circumference(radius))
    print("The surface area is", surface_area(radius))
    print("The volume is", volume(radius))
