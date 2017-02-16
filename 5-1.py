'''

Exercise 5-1: Person class

Create an Person class with a method to check if a person is equal than 
another one.

equals operator: 
  __eq__(self, other)

Define Person class first: 

class Person:
   def __init__(self, name)
   def __eq__(self,other)

To test equality in code:

p1 = Person("Bill")
p2 = Person("Bill")
p3 = Person("Joe")
p1 == p2
p3 == p2
'''
class person:
   def __init__(self,name):
      self.name=name
   def __eq__(self,other):
      if self.name == other.name:
         return True


p1 = person("Bill")
p2 = person("Bill")
p3 = person("Joe")

print(p1 == p2)
print(p3 == p2)