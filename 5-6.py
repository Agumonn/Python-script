'''
Exercise 5-6: Triangle class

Plan, create and test a class called Triangle.

* calculate the Area of Triangle with two different way
* calculate also the total perimeter of the Triangle

See the possible properties by reading base theory from here: 
https://www.mathsisfun.com/algebra/trig-area-triangle-without-right-angle.html
https://www.mathsisfun.com/geometry/herons-formula.html
https://www.mathsisfun.com/triangle.html

this script calculates the area of of 2 different triangles in different ways
'''

import math
class Triangle:
   def __init__(self,luku):
      self.luku= luku
   def __mul__(self,other):
      area = self.luku*other.luku
      return area
   def __add__(self,other):
      peri = self.luku + other.luku
      return peri
   def repr(self):
      return self.luku

height=int(input("tell me the height of the triangle: "))
width=int(input("tell me the width of the triangle: "))

height = Triangle(height)
width = Triangle(width)

print("area is=", height * width / 2 )
print("calculated by height*width/2")



#the second triangle Area calculated by = 0.5*side a*side b* sin (angle)

lenghta=int(input("length of the side of the triangle: "))
lengthb=int(input("and the length of the other side: "))
angle = float(input("Please enter the measurement of your angle in degrees."))

a = math.radians(angle)#change to radians
d = float(math.sin(a))#sin operation d is the value of sin(angle)
lenghta = Triangle(lenghta)
lengthb= Triangle(lengthb)

midarea=(lenghta* lengthb/ 2 )


print("area is=", midarea * d )
print("calculated by Area = 0.5*side a*side b* sin (angle)")



