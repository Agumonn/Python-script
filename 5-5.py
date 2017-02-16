'''
Exercise 5-5: Student sorting

Sorting Student objects in the list

Create an Student class with the properties
* name and
* grade properties

Then add some students into the list and sort these students
using their age and grade properties. 

class Student:
    # name, grade

student_list = [Student('jim', 4),Student('jane', 3),Student('tim', 5),Student('kim',1),Student('ann',2)]
# TODO: sort student with sorted() method

Sorted by age and grade:

[('ann', 2), ('jane', 3), ('jim', 4), ('kim', 1), ('tim', 5)]
[('kim', 1), ('ann', 2), ('jane', 3), ('jim', 4), ('tim', 5)]
'''
class Student:
   def __init__(self, name, grade):
      self.name = name
      self.grade = grade
   def __repr__(self):
      return repr((self.name, self.grade))

def name(lista):
   return lista.name     
def grade(lista):
   return lista.grade   


lista = Student('jim', 4), Student('jane', 3), Student('tim', 5), Student('kim', 1), Student('ann', 2)


print("sorted by name: ")
print(sorted(lista, key=name))
print("sorted by grade: ")
print(sorted(lista, key=grade))