Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> r = float(input("The radius of a circle:"))
The radius of a circle:1.1
>>> area = math.pi*r**2
>>> print("Area of a circle with radius "+ str(r) +" is:%.16f" %area)
Area of a circle with radius 1.1 is:3.8013271108436504
>>> 