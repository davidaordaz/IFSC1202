import math

print("Great Circle Calculator")
radius = float(input("Enter Radius of Sphere: "))
x1 = float(input("Starting Point - Enter Latitude: "))
y1 = float(input("Starting Point - Enter Longitude: "))
x2 = float(input("Ending Point - Enter Latitude: "))
y2 = float(input("Ending Point - Enter Longitude: "))

from math import sin
from math import cos
from math import acos
from math import pi

x1 *= pi/180
x2 *= pi/180
y1 *= pi/180
y2 *= pi/180
d = radius * acos(sin(x1)*sin(x2) + cos(x1)*cos(x2)*cos(y1-y2))

print("The Great Circle Distance is",round(abs(d),2))