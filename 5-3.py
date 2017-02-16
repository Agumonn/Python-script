'''
Exercise 5-3: Create calculator using operator module

The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y. 

using the following operators:

operator.__add__(a, b)

    Return a + b, for a and b numbers.

operator.__mul__(a, b)


TODO: 
* __add__() to implement a+b
* __mul__() to implement a*b

class Calculator:
    # TODO: methods for __add__ and __mul__
    # https://docs.python.org/3.5/library/operator.html

Test with the following program:

c1 = Calculator(15)
c2 = Calculator(10)

print("c1+c2=", c1+c2)
print("c1*c2=", c1*c2)

Output:

c1+c2=25
c1*c2=150
'''
class Calculator:
   def __init__(self, luku):
      self.luku = luku
   def str(self):
      return("%i" % (self.luku))
   def __add__(self, other):
      sum = self.luku+ other.luku
      return sum
   def __mul__(self, other):
      multi = self.luku* other.luku
      return multi
   def repr(self):
      return self.luku

c1 = Calculator(15)
c2 = Calculator(10)

print("c1+c2=", c1+c2)
print("c1*c2=", c1*c2)
