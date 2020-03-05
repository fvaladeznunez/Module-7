# Fernando Valadez-Nunez
# 02/27/2020

# Problem 1 - Write a function areaOfCircle (r) which returns the area of a
# circle of radius r.

import math
def areaOfCircle(r):
  return math.pi*r**2
  
radius = int(input("What is the radius of your circle? "))

print(areaOfCircle(radius))
