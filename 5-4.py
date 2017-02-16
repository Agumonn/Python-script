'''
Exercise 5-4: Worker sorting

Use Worker class from the exercise 5-2.
Add Worker object into the list.

Sort this list based on name and salary of the workers. 

Help for sorting:

https://docs.python.org/3/howto/sorting.html#sortinghowto
http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/

persons=list()
persons.append(Worker("Bill","FullTime", 4500))
# etc.

# TODO: sort workers by name or salary

Output should be:

sorted by name:

[('Ann', 'Hourly', 3300), ('Bill', 'FullTime', 4500), ('Calle', 'FullTime', 3900), ('Jill', 'FullTime', 4100), ('John', 'PartTime', 2900), ('Mary', 'Hourly', 2600)]

sorted by salary:

[('Mary', 'Hourly', 2600), ('John', 'PartTime', 2900), ('Ann', 'Hourly', 3300), ('Calle', 'FullTime', 3900), ('Jill', 'FullTime', 4100), ('Bill', 'FullTime', 4500)]
'''


class Worker:
   def __init__(self,name,contract,salary):
      self.name=name
      self.contract=contract
      self.salary=salary
   def __repr__(self):
      return repr((self.name, self.contract, self.salary))
   def __lt__(self, other):
      return self.name < other.name
def name(persons):
   return persons.name     
def salary(persons):
   return persons.salary   
 
persons = list()
persons.append(Worker("Bill","FullTime", 4500))
persons.append(Worker("John","PartTime", 2900))
persons.append(Worker("Calle","FullTime", 3900))
persons.append(Worker("Mary","Hourly", 2600))
persons.append(Worker("Jill","FullTime", 4100))
persons.append(Worker("Ann","Hourly", 3300))

print("sorted by name: ")
print(sorted(persons, key=name))
print("sorted by salary: ")
print(sorted(persons, key=salary))